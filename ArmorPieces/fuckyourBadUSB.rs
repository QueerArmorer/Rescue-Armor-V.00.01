use evdev::{Device, DeviceWrapper, InputEvent, UInputDevice, UInputDeviceBuilder};
use std::collections::VecDeque;
use std::fs;
use std::io::Read;
use std::process::Command;

fn main() {
    let password = "mypassword".as_bytes();
    let max_attempts = 5;
    let mut attempts = 0;

    let mut devices: Vec<DeviceWrapper> = Vec::new();

    // Look for the inputs
    loop {
        // Get a list
        let device_paths = match fs::read_dir("/dev/input") {
            Ok(paths) => paths,
            Err(e) => {
                eprintln!("Failed to read input device directory: {}", e);
                continue;
            }
        };

        // Open all of them
        for device_path in device_paths {
            let device_path = match device_path {
                Ok(p) => p.path(),
                Err(e) => {
                    eprintln!("Failed to get device path: {}", e);
                    continue;
                }
            };

            // Check
            if devices.iter().any(|d| d.device.device_path() == device_path) {
                continue;
            }

            // Open devices
            let device = match Device::open(&device_path) {
                Ok(d) => d,
                Err(e) => {
                    eprintln!("Failed to open device '{}': {}", device_path.display(), e);
                    continue;
                }
            };

            // Check if it's a keyboard
            if !device.has_key_events() {
                continue;
            }

            // And we're off to the races
            let mut device_wrapper = DeviceWrapper::new(device).unwrap();
            device_wrapper.enable_event_retrieval().unwrap();
            devices.push(device_wrapper);

            println!("New keyboard detected: {}", device_path.display());
        }

        // Check for password inputs
        let mut input_events: VecDeque<InputEvent> = VecDeque::new();
        for device_wrapper in &devices {
            while let Some(event) = device_wrapper.next_event().unwrap() {
                input_events.push_back(event);
            }
        }

        // Check if the password has been entered
        let mut typed_password: Vec<u8> = Vec::new();
        for event in input_events {
            if event.is_key() && event.value != 0 {
                typed_password.push(event.code);
            } else if event.is_syn() {
                // Check if the entered password is correct
                if typed_password.as_slice() == password {
                    println!("Password accepted!");
                    // Reset the password and attempts counter
                    typed_password.clear();
                    attempts = 0;
                } else {
                    attempts += 1;
                    println!("Incorrect password (attempt {} of {})!", attempts, max_attempts);
                    // Reset the password
                    typed_password.clear();

                    if attempts >= max_attempts {
                        // Reboot the computer
                        println!("Max password attempts reached. Rebooting...");
                        Command::new("reboot").spawn().unwrap();
                        return;
                    }
                }
            }
        }
    }
}


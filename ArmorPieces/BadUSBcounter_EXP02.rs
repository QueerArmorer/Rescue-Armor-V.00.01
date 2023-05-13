use evdev::Device;
use evdev::enums::EventCode;
use gtk::prelude::*;
use gtk::{Button, Entry, Window, WindowType};
use std::process::Command;

const PASSWORD: &str = "your_password";
const MAX_PASSWORD_ATTEMPTS: usize = 5;

fn main() {
    gtk::init().expect("Failed to initialize GTK.");

    // Create a window
    let window = Window::new(WindowType::Toplevel);
    window.set_title("Password Window");
    window.set_default_size(300, 150);
    window.set_resizable(false);

    // Create an entry field for the password
    let entry = Entry::new();
    entry.set_visibility(false); // Hide entered characters
    window.add(&entry);

    // Create a submit button
    let button = Button::with_label("Submit");
    window.add(&button);

    // Disable window switching
    window.set_keep_above(true);
    window.set_decorated(false);

    // Track the number of password attempts
    let mut password_attempts = 0;

    // Connect to the keyboard device
    let mut devices = evdev::enumerate();
    while let Some(device) = devices.next() {
        if device.name().contains("keyboard") {
            // Handle keyboard events
            handle_keyboard_events(device, &entry, &button, &mut password_attempts);
        }
    }

    // Show the window and start the GTK main event loop
    window.show_all();
    gtk::main();
}

fn handle_keyboard_events(
    device: Device,
    entry: &Entry,
    button: &Button,
    password_attempts: &mut usize,
) {
    let fd = device.fd().unwrap();
    let name = device.name().to_owned();

    // Spawn a new thread to handle device events
    std::thread::spawn(move || {
        let mut buffer = String::new();

        loop {
            let event = device.next_event().unwrap();
            if let EventCode::EV_KEY(key_event) = event.event_code {
                if key_event.value == 1 {
                    // Key pressed event
                    let key_code = key_event.key_code as usize;
                    if key_code == evdev::enums::Key::KEY_ENTER as usize {
                        // Enter key pressed
                        if buffer == PASSWORD {
                            // Password correct
                            println!("Password correct!");
                            break;
                        } else {
                            // Wrong password
                            println!("Wrong password!");
                            buffer.clear();
                            *password_attempts += 1;

                            if *password_attempts >= MAX_PASSWORD_ATTEMPTS {
                                // Disable the keyboard after maximum attempts reached
                                disable_keyboard(&name);
                                println!("Maximum password attempts reached. Keyboard disabled.");
                                break;
                            }
                        }
                    } else if key_code == evdev::enums::Key::KEY_BACKSPACE as usize {
                        // Backspace key pressed
                        buffer.pop();
                    } else {
                        // Other keys pressed
                        let key = evdev::enums::Key::from(key_code);
                        buffer.push_str(&key.to_string());
                    }
                }
            }
        }

        gtk::main_quit();
    });
}

fn disable_keyboard(name: &str) {
    // Execute system command to disable the keyboard device
    let output = Command::new("xinput")
        .arg("disable")
        .arg(name)
        .output()
        .expect("Failed to execute command.");

    if !output.status.success() {
        panic!("Failed to disable the keyboard.");
    }
}


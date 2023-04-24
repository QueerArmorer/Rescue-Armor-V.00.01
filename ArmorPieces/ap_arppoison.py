import subprocess

print("Please make sure you are following best infosec practices before running this script.")

#Fuck it we ball?
interfaces = subprocess.check_output(['arpwatch', '-i'], universal_newlines=True).split("\n")[1:-1]
print("Available interfaces:")
for i, interface in enumerate(interfaces):
    print(f"{i + 1}. {interface}")

selected_interface = int(input("Please select an interface: ")) - 1
selected_interface_name = interfaces[selected_interface]

print(f"Selected interface: {selected_interface_name}")

subprocess.call(["sudo", "arpwatch", "-d", "-i", selected_interface_name])

#The big ass loop. Code go spinny.

detected = False

while not detected:
    print("Checking for ARP poisoning...")
    output = subprocess.check_output(['tail', '-n', '1', '/var/log/syslog'], universal_newlines=True)
    if "arpwatch" in output and "added" in output:
        detected = True
        print("ARP poisoning detected!")
        print(output)
    elif "arpwatch" in output and "deleted" in output:
        print("ARP table entry removed.")
    else:
        print("No ARP poisoning detected.")

print("Stopping ARPwatch...")
subprocess.call(["sudo", "killall", "arpwatch"])

print("ARPwatch stopped.")


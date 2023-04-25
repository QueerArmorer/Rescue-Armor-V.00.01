import os
import urllib.request
import subprocess

lastpass_url = "https://download.cloud.lastpass.com/windows_installer/lastpass.exe"
lastpass_file = "lastpass.exe"
lastpass_folder = os.path.join("C:", os.sep, "Program Files (x86)", "LastPass")

# First up, check if the thing exists
if not os.path.exists(lastpass_folder):
    # Ask to install
    user_input = input("LastPass folder doesn't exist. Do you want to install it? (y/n): ")
    if user_input.lower() == 'y':
        # Download
        print("Downloading LastPass installation file...")
        urllib.request.urlretrieve(lastpass_url, lastpass_file)

        # Run the Install
        print("Running LastPass installation file...")
        subprocess.call([lastpass_file, "/S"])

        # Verify
        if os.path.exists(lastpass_folder):
            print("LastPass installed successfully!")

            # Is it lazy? Or is it "they made an entire website for a reason" and not reinventing the wheel? You judge I'm too lazy to.
            print("Please log in to your LastPass account at https://lastpass.com/")
            subprocess.call(["start", "https://lastpass.com/"])
        else:
            print("Failed to install LastPass.")
    else:
        print("LastPass installation canceled.")
else:
    print("LastPass is installed.")


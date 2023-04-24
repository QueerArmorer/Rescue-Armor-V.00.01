import os
import urllib.request
import subprocess

avast_path = "C:\\Program Files\\AVAST Software\\Avast\\avastui.exe"
avast_url = "https://files.avast.com/iavs9x/avast_free_antivirus_setup_online.exe"

# Check if Avast is installed
if not os.path.isfile(avast_path):
    # Ask before just installing
    answer = input("Avast is required for Rescue Armor. Do you want to download and install Avast? (y/n): ")
    if answer.lower() == "y":
        # Download the thing
        avast_installer_path = os.path.join(os.getcwd(), "avast_installer.exe")
        urllib.request.urlretrieve(avast_url, avast_installer_path)

        # Install the thing
        subprocess.run([avast_installer_path, "/quiet", "/norestart"])
        print("Avast installed successfully.")
        os.remove(avast_installer_path)
    else:
        print("Without Avast, Rescue Armor cannot be installed.")
else:
    print("Avast is already installed.")


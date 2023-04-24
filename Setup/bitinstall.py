import os
import subprocess
import urllib.request
import re

# What're we doing
BD_INSTALLER_URL = "https://download.bitdefender.com/windows/desktop/connect/cl/64/bitdefender_ts_26_64b.exe"
BD_INSTALLER_NAME = "bitdefender_ts_64b.exe"

# Check if we need to
def is_bitdefender_installed():
    try:
        with open(os.devnull, 'w') as null:
            subprocess.check_call(['powershell', '-command', 'Get-ItemProperty HKLM:\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName, DisplayVersion, Publisher, InstallDate | Where-Object {$_.DisplayName -like "Bitdefender*"}'], stdout=null, stderr=null)
            return True
    except subprocess.CalledProcessError:
        return False

# Ask permission
def ask_to_install_bitdefender():
    print("Bitdefender Free Antivirus is required to continue with the Rescue Armor installation.")
    response = input("Do you want to install Bitdefender now? (y/n): ")
    return response.lower() == "y"

# Download the thing
def download_bitdefender_installer():
    urllib.request.urlretrieve(BD_INSTALLER_URL, BD_INSTALLER_NAME)

# Install Bitdefender
def install_bitdefender():
    download_bitdefender_installer()
    try:
        with open(os.devnull, 'w') as null:
            subprocess.check_call([BD_INSTALLER_NAME, '/quiet', '/l*v', 'bitdefender-install.log'], stdout=null, stderr=null)
    except subprocess.CalledProcessError:
        print("Bitdefender installation failed.")

# The actual engine
if not is_bitdefender_installed():
    if ask_to_install_bitdefender():
        install_bitdefender()
    else:
        print("Warning: Not installing Bitdefender means abandoning the Rescue Armor installation.")
else:
    print("Bitdefender is already installed.")


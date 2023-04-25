import os
import urllib.request

# Download
print("Downloading NordVPN installer...")
url = "https://downloads.nordcdn.com/apps/windows/10/NordVPN/latest/NordVPNSetup.exe"
filename = "NordVPNSetup.exe"
urllib.request.urlretrieve(url, filename)

# Install
print("Installing NordVPN...")
os.system(f"start /wait {filename} /silent")

# Clean up
print("Cleaning up...")
os.remove(filename)

print("NordVPN has been installed successfully.")

# Still to lazy to do this, kick to website.
print("Creating a NordVPN account...")
webbrowser.open_new_tab("https://join.nordvpn.com/signup/")

print("NordVPN has been installed successfully. Please create an account on the NordVPN website.")

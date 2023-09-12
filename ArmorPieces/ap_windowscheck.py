import os
import subprocess
import requests
from bs4 import BeautifulSoup

# What's the deal, what's your bag, what's your flavor?
def get_windows_version():
    version_info = os.sys.getwindowsversion()
    return f"{version_info.major}.{version_info.minor}"

# Look if bill gates is going to pay to keep the information online I'm going to use it for free
def get_latest_windows_version():
    microsoft_url = "https://www.microsoft.com/en-us/software-download/windows10"
    response = requests.get(microsoft_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    latest_version_element = soup.find("div", class_="sample-item-details")
    latest_version = latest_version_element.find("strong").text.strip()
    return latest_version

# Fuck things up (update Windows using PowerShell)
def update_windows_with_powershell():
    update_script = '''
    # Check for updates and install
    Install-PackageProvider -Name NuGet -Force -Scope CurrentUser
    Install-Module -Name PSWindowsUpdate -Force -Scope CurrentUser
    Get-WindowsUpdate -Install -AcceptAll
    '''
    subprocess.run(["powershell", "-Command", update_script], shell=True)

if __name__ == "__main__":
    current_version = get_windows_version()
    latest_version = get_latest_windows_version()

    print(f"Current Windows Version: {current_version}")
    print(f"Latest Windows Version: {latest_version}")

    if current_version < latest_version:
        print("An update is available. Updating Windows...")
        update_windows_with_powershell()
        print("Windows has been updated.")
    else:
        print("No update available.")


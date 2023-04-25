import os
import urllib.request
import subprocess

protonvpn_url = "https://protonvpn.com/download/ProtonVPN_win_latest.exe"
protonvpn_file = "ProtonVPN.exe"
protonvpn_folder = os.path.join("C:", os.sep, "Program Files (x86)", "ProtonVPN")

# Check if it's installed
if not os.path.exists(protonvpn_folder):
    # Ask nicely because autonomy
    user_input = input("ProtonVPN isn't installed. Do you want to install it? (y/n): ")
    if user_input.lower() == 'y':
        # Download
        print("Downloading ProtonVPN installation file...")
        urllib.request.urlretrieve(protonvpn_url, protonvpn_file)

        # Install
        print("Running ProtonVPN installation file...")
        subprocess.call([protonvpn_file, "/S"])

        # Verify
        if os.path.exists(protonvpn_folder):
            print("ProtonVPN installed successfully!")

            # I cannot be arsed to do account creation programmatically, kick them to the website
            print("Please create your ProtonVPN account. There are pay options that will also give you an extended encrypted email address, but they also offer free VPN services to everyone.")
            subprocess.call(["start", "https://account.protonvpn.com/signup"])
        else:
            print("Failed to install ProtonVPN.")
    else:
        print("ProtonVPN installation canceled.")
else:
    print("ProtonVPN is installed.")


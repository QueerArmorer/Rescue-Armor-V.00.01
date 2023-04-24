import os
import subprocess

# Check if we need to
gmer_path = "C:\\GMER\\gmer.exe"
if os.path.exists(gmer_path):
    print("GMER is already installed.")
else:
    # Ask permission
    permission = input("GMER is required for Rescue Armor to work. Do you want to install GMER now? (y/n): ")
    if permission.lower() == "y":
        # Download GMER
        url = "https://gmer.net/gmer.zip"
        download_path = os.path.join(os.getcwd(), "gmer.zip")
        subprocess.run(["powershell", "-Command", f"(New-Object System.Net.WebClient).DownloadFile('{url}', '{download_path}')"])

        # Extract
        extract_path = os.path.join(os.getcwd(), "GMER")
        subprocess.run(["powershell", "-Command", f"Expand-Archive '{download_path}' '{extract_path}'"])

        # Path check on Cereal
        add_to_path = input("We recommend adding GMER to PATH for this install, which basically makes it easier to call with other programs. Do you want to add GMER to your system PATH? (y/n): ")
        if add_to_path.lower() == "y":
            os.environ["Path"] += os.pathsep + os.path.join(os.getcwd(), "GMER")

        print("GMER has been installed successfully.")
    else:
        # GMER's required
        warning = input("Warning: GMER is required for Rescue Armor to work. Are you sure you don't want to install GMER? (y/n): ")
        if warning.lower() == "n":
            # Download GMER, for real this time
            url = "https://gmer.net/gmer.zip"
            download_path = os.path.join(os.getcwd(), "gmer.zip")
            subprocess.run(["powershell", "-Command", f"(New-Object System.Net.WebClient).DownloadFile('{url}', '{download_path}')"])

            extract_path = os.path.join(os.getcwd(), "GMER")
            subprocess.run(["powershell", "-Command", f"Expand-Archive '{download_path}' '{extract_path}'"])

            # Back again I see
            add_to_path = input("Do you want to add GMER to your system PATH? (y/n): ")
            if add_to_path.lower() == "y":
                os.environ["Path"] += os.pathsep + os.path.join(os.getcwd(), "GMER")

            print("GMER has been installed successfully.")
        else:
            print("GMER is required for Rescue Armor to work. Please install GMER.")


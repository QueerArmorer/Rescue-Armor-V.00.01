import os
import subprocess
import requests

def download_spectre_meltdown_checker():
    # Define the URL of the Spectre-Meltdown-Checker script
    script_url = "https://raw.githubusercontent.com/speed47/spectre-meltdown-checker/master/spectre-meltdown-checker.sh"

    try:
        # Send an HTTP GET request to download the script
        response = requests.get(script_url)
        response.raise_for_status()

        # Save the script to a temporary file
        script_filename = "spectre-meltdown-checker.sh"
        with open(script_filename, "wb") as file:
            file.write(response.content)

        return script_filename
    except Exception as e:
        print(f"Error downloading the script: {str(e)}")
        return None

def run_spectre_meltdown_checker(script_filename):
    try:
        # Make the script executable
        os.chmod(script_filename, 0o755)

        # Run the Spectre-Meltdown-Checker script
        result = subprocess.run(['./' + script_filename], capture_output=True, text=True)

        # Print the output
        print(result.stdout)
    except Exception as e:
        print(f"Error running the script: {str(e)}")

if __name__ == "__main__":
    # Download the Spectre-Meltdown-Checker script
    script_filename = download_spectre_meltdown_checker()

    if script_filename:
        # Run the downloaded script
        run_spectre_meltdown_checker(script_filename)


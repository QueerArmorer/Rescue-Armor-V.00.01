import os
import subprocess

def format_drive(drive_letter, project_name):
    # Is this loss?
    if not os.path.exists(drive_letter):
        print("Invalid drive letter.")
        return

    # Check yo self
    confirmation = input("Are you sure you want to format this drive? All data will be permanently deleted. (y/n): ")
    if confirmation.lower() != "y":
        return

    # We do a little naming
    project_name = input("Please enter a name for the project: ")

    # Wreck yo self
    print("Formatting drive...")
    cmd = f"format {drive_letter} /FS:NTFS /V:\"{project_name} Rescue Armor reference\" /Q"
    subprocess.call(cmd, shell=True)

    print(f"Drive {drive_letter} has been formatted and labeled as \"{project_name} Rescue Armor reference\".")
    print("Thank you for using Rescue Armor.")

if __name__ == "__main__":
    # Check check yo
    available_drives = [f"{chr(i)}:" for i in range(65,91) if os.path.exists(f"{chr(i)}:")]

    # Printing and running and printing and running ...
    if not available_drives:
        print("No USB drives found.")
    else:
        print("The following USB drives are available:")
        print("\n".join(available_drives))

        # Ask for user input for drive selection
        drive_letter = input("Please enter the drive letter you want to use: ").upper()

        format_drive(drive_letter, "")


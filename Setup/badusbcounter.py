import os
import wmi
import schedule
import time
import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")

# Fuck BadUSB
def check_keyboards():
    # Open the text file
    with open(known_keyboards_file, 'r') as f:
        known_keyboards = int(f.read())

    c = wmi.WMI()

    # Get the current number
    keyboard_count = sum(1 for k in c.Win32_Keyboard())

    # Check if there are more keyboards than known keyboards
    if keyboard_count > known_keyboards:
        print('Warning: Possible BadUSB attack detected!')  # Replace with your desired alert mechanism
        speak.Speak('Warning: Possible BadUSB attack detected!')  # Speech alert

# Menu Pathing
def display_menu(path):
    while True:
        # Print the contents of where we are
        print("Current directory: ", path)
        print("Choose a file or folder to navigate to:")
        items = os.listdir(path)
        for i, item in enumerate(items):
            print(f"{i + 1}. {item}")
        print("b. Back")

        # Get user input
        user_input = input("Enter selection: ")
        try:
            selection = int(user_input)
            if 1 <= selection <= len(items):
                # File Path
                file_path = os.path.join(path, items[selection - 1])
                if os.path.isfile(file_path):
                    return file_path
                # Display the menu
                elif os.path.isdir(file_path):
                    path = file_path
            elif user_input.lower() == "b":
                # navigation
                path = os.path.dirname(path)
            #Error handling
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid selection. Please try again.")

# Get the file path
path = os.getcwd() 
known_keyboards_file = display_menu(path)

# Schedule it to run every 3 minutes
schedule.every(3).minutes.do(check_keyboards)

# Run the scheduled tasks indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)


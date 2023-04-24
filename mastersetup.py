import os

# Path to the Setup directory
setup_dir = os.path.join(os.getcwd(), "Setup")

# Check if the Setup directory exists
if not os.path.exists(setup_dir):
    print("Error: Setup directory does not exist.")
    exit()

# List all the files in the Setup directory
files = os.listdir(setup_dir)

# Loop through each file in the Setup directory
for file in files:
    # Check if the file is a Python script
    if file.endswith(".py"):
        # Construct the full path to the file
        file_path = os.path.join(setup_dir, file)
        
        # Print the name of the script that is being run
        print(f"Running {file}...")

        # Try to run the script
        try:
            exec(open(file_path).read())
            print(f"{file} ran successfully!")
        except Exception as e:
            print(f"Error running {file}: {e}")

# Done running all scripts
print("All scripts in Setup directory have been run once.")


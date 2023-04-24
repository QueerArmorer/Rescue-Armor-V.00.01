import os

folder_path = os.path.join(os.path.dirname(__file__), "Armor Pieces")

if not os.path.exists(folder_path):
    print("Error: The folder 'Armor Pieces' could not be found.")
else:
    print("Armor Pieces folder found!")
    print("------------------------------------------\n")

    # Big ass list
    files = os.listdir(folder_path)

    # Only Armor Pieces
    ap_files = [file for file in files if file.startswith("ap_")]

    # Run that shit
    for file in ap_files:
        try:
            print(f"Running script: {file}")
            exec(open(os.path.join(folder_path, file)).read())
            print(f"{file} completed successfully!\n")
        except Exception as e:
            print(f"{file} encountered an error:")
            print(e)
            print("\n")


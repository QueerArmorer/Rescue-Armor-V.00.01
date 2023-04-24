import hashlib
import os
import getpass

password = getpass.getpass(prompt="Enter password for RescueArmor folder: ")

# Passwords are key
os.system(f'7z x -p{password} -y RescueArmor.7z')
with open('RescueArmor/file_list.txt') as f:
    files_to_check = f.read().splitlines()

# Check with a folder
if not os.path.exists('checkfolder'):
    os.makedirs('checkfolder')

# Make some hash
for file in files_to_check:
    # Rolling the joint
    hasher = hashlib.sha256()
    with open(file, 'rb') as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            hasher.update(data)
    current_hash = hasher.hexdigest()

    # Grab a backup from an older brother
    with open(f'RescueArmor/{file}.hash') as f:
        known_good_hash = f.read()

    # Smoke both, right?
    if current_hash != known_good_hash:
        print(f'Changes made to {file}, this system is compromised, a full reset is recommended.')

# Delet the extras
os.system('rm -rf checkfolder')


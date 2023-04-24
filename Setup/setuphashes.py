import hashlib
import os
import getpass
import zipfile

# Let's go searching for reference files
directory = r'C:\Windows\System32'

# Where we're going
output_directory = None

# Gimme dem USBs
drives = os.listdir('/media')

# Grab that reference
for drive in drives:
    if drive.endswith('Rescue Armor reference'):
        output_directory = f'/media/{drive}'
        break

if output_directory is None:
    print('Error: No USB drive with a name ending in "Rescue Armor reference" found.')
else:
    print(f'Output directory: {output_directory}')

# Saaaaaaaaaaaay sooooooooooooooooooomething ... like your password ...
password = getpass.getpass('Enter password for encryption: ')

# Now put everything where I told you
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Get that list going ...
filenames = []

# We make some good hash
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        with open(filepath, 'rb') as f:
            hash = hashlib.sha256(f.read()).hexdigest()
        output_filename = os.path.join(output_directory, file + '.hash')
        with open(output_filename, 'w') as f:
            f.write(hash)
        filenames.append(filepath)

# What the fuck did we just smoke?
file_list_filename = os.path.join(output_directory, 'file_list.txt')
with open(file_list_filename, 'w') as f:
    for filename in filenames:
        f.write(filename + '\n')

# Bruh you don't need to know.
zip_filename = os.path.join(output_directory, 'hashes.zip')
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(output_directory):
        for file in files:
            zf.write(os.path.join(root, file), arcname=file)

# Lock it up, dude's sus AF.
encrypted_zip_filename = os.path.join(output_directory, 'hashes.zip.enc')
with zipfile.ZipFile(encrypted_zip_filename, 'w', zipfile.ZIP_DEFLATED) as zf:
    zf.setpassword(password.encode())
    zf.write(zip_filename, arcname='hashes.zip')

# Delet
os.remove(zip_filename)

print('Hashes saved to {output_directory} and encrypted with your password.'.format(encrypted_zip_filename))


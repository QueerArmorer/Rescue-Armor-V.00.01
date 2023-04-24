import requests
import os
import time
import shutil

# Literally War and Peace
url = 'https://www.gutenberg.org/files/2600/2600-0.txt'
response = requests.get(url)
text = response.text

# "I wish I was big"
target_file_size = 200 * 1024 * 1024  # 200 MB
while len(text.encode('utf-8')) < target_file_size:
    text += text

# Write to file
with open('war_and_peace.txt', 'w', encoding='utf-8') as f:
    f.write(text)

# Start the clock
start_time = time.time()

# Move it, pal
os.chdir('..')
shutil.move('war_and_peace.txt')

# And stop
transfer_time = time.time() - start_time

# New thing, just like the old thing
with open('testtime.txt', 'w') as f:
    f.write(f'Transfer time: {transfer_time} seconds')

# Wait, check the old thing first.
with open('reference_time.txt', 'r') as f:
    reference_time = float(f.read().split(': ')[-1].split()[0])

# Is it like the old thing?
error_threshold = 0.05  # 5%
if abs(transfer_time - reference_time) / reference_time > error_threshold:
    print('Error: Transfer time is more than 5% different from the reference time. There may be a problem')
else:
    print('Rescue Armor does not detect anything wrong with this hard drive.')

# Delet this
shutil.rmtree('war_and_peace.txt')

print('Reference test done.')

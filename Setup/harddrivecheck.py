import requests
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
shutil.move('war_and_peace.txt', '..')

# And stop
transfer_time = time.time() - start_time

# Referentializationism
with open('reference_time.txt', 'w') as f:
    f.write(f'Transfer time: {transfer_time} seconds')

# Delet this
shutil.rmtree('war_and_peace.txt')

print('Reference test done.')


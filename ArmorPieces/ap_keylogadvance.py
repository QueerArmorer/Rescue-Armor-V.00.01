import random
import time
import string
import os
import keyboard

# Poetry, yo
word_list = []
for i in range(10):
    word = ""
    for j in range(random.randint(3, 5)):
        word += random.choice(string.ascii_lowercase)
    word_list.append(word)
    if i < 9:
        word_list.append("   ")

# And now, we type
for word in word_list:
    for letter in word:
        keyboard.press(letter)
        keyboard.release(letter)
        time.sleep(0.25)
    if word != "   ":
        keyboard.press_and_release("space")

# Make "the list"
encrypted_list = []
for word in word_list[::2]:
    variants = []
    # Add the original back
    variants.append(word)
    # Add Atbash
    atbash = "".join([chr(219 - ord(c)) if c.islower() else c for c in word])
    variants.append(atbash)
    # Add Reverse cipher
    reverse = word[::-1]
    variants.append(reverse)
    # Add Caesar cipher
    for i in range(1, 26):
        caesar = ""
        for c in word:
            if c.isalpha():
                caesar += chr((ord(c) - 97 + i) % 26 + 97)
            else:
                caesar += c
        variants.append(caesar)
    # Add substitutions
    substitutions = []
    for i in range(26):
        cipher = "".join([chr((ord(c) - 97 + i) % 26 + 97) if c.islower() else c for c in word])
        substitutions.append(cipher)
    variants += substitutions
    encrypted_list.append(variants)

# Go out searching. A lot.
search_term = input("Enter search term: ")
results = []
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".txt") or file.endswith(".log"):
            with open(os.path.join(root, file), "r") as f:
                contents = f.read()
                if search_term in contents:
                    results.append(os.path.join(root, file))

# Are we fucked?
if results:
    print("Rescue Armor has discovered a KeyLog, which indicates your system is compromised and likely has key logging software. Change your passwords and reset your system.")
    for result in results:
        print(result)
else:
    print("No results found, Rescue Armor is intact.")


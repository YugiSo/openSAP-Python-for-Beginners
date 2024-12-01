# Week 3 - Assignment

import string

msg = input("Please enter a sentence: ")
msg = msg.lower()

SHIFT: int = 5
enc = ''

for i in range(len(msg)):
    char = msg[i]

    if char in string.punctuation or char in string.whitespace:
        enc += char

    if char.isalpha():
        enc += chr((ord(char) + SHIFT - 97) % 26 + 97)

print(f'The encrypted msg is: {enc}')
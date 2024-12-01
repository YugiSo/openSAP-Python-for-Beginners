# Week 3 - Bonus Assignement

import string

SHIFT = int(input("Please enter the number of places to shift: "))

if SHIFT < 0 or SHIFT > 25:
    print("You need to enter a number between 0 and 25!")

MSG = input("Please enter a sentence: ")
MSG = MSG.lower()

ENC = ""
for i in range(len(MSG)):
    ch = MSG[i]
    
    if ch in string.punctuation or ch in string.whitespace:
        ENC += ch

    if ch.isalpha():
        ENC += chr((ord(ch) + SHIFT - 97) % 26 + 97)
        
        
print(f'The encrypted sentence is: {ENC}')
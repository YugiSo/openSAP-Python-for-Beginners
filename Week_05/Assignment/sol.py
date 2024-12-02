# Week 5 - Assignment

import string

alpha = string.ascii_lowercase

def calculate_shifts(letter: str) -> int:
    return alpha.index(letter)

def encrypt_letter(letter: str, shift: int) -> str:
    if letter.isalpha():
        idx = alpha.index(letter)
        idx = (idx + shift) % 26
        return alpha[idx]
    else:
        return letter

def encrypt_text(msg: str, keyword: str) -> str:
    msg = msg.lower()
    keyword = keyword.lower()

    enc_msg = ''
    for idx, ch in enumerate(msg):
        key = keyword[idx % len(keyword)]
        enc_msg += encrypt_letter(ch, calculate_shifts(key))

    return enc_msg


text = input('Which text should be encrypted: ')
key = input('Which keyword should be used? ')

print(encrypt_text(text, key))
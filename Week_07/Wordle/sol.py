# Week 7 - Final-Exam

from collections import Counter
import random


def wordList() -> list:
    with open('Week_07/Wordle/5_letter_words.txt') as file:
        data = file.read().split()

    return data

def getRandomWord(words: list) -> str:
    return random.choice(words)

def isWordReal(guess: str, words: list) -> bool:
    return guess in words

def checkGuess(guess: str, goal: str) -> str:
    
    res = ''
    pool = Counter(ch1 for ch1, ch2 in zip(goal, guess) if ch1 != ch2)

    # print(pool)

    for ch1, ch2, in zip(goal, guess):
        if ch1 == ch2:
            res += 'X'
        elif ch2 in goal and pool[ch2] > 0:
            res += 'O'
            pool[ch2] -= 1
        else:
            res += '_'

    return res

def Guess(data: list) -> str:
    while True:
        guess = input('Please enter a guess: ').lower()

        if isWordReal(guess, data):
            break

        print("That's not a real word!")

    return guess

def playWordle():

    words = wordList()
    goal = getRandomWord(words)

    # print(goal)

    turns = 0
    while turns < 6:
        guess = Guess(words)

        res = checkGuess(guess, goal)
        print(res)

        if res == 'XXXXX':
            print('You Won!')
            break

        turns = turns + 1

    if turns >= 6:
        print('\nYou Lost!')
        print(f'The word was: {goal}')


playWordle()
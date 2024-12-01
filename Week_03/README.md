## Python for Begineers - Week 3

### Unit 1: Exercise

Write a program that asks the user for given name, surname and field of study for a student. Store this data in a tuple and print the tuple. Below is an example execution of the program.
```text
    Please enter the given name of the student: Harry
    Please enter the surname of the student: Potter
    Please enter the field of study of the student: Defence Against the Dark Arts
    ('Harry', 'Potter', 'Defence Against the Dark Arts')
```

[Solution](3.1/sol.py)
___
### Unit 2: Exercise

One of the nice features of Python is that it supports [Unicode](https://en.wikipedia.org/wiki/Unicode). Therefore it is possible to use emojis just like other characters in strings. In this exercise you will use this feature to build an emoji translator.

Below is a dictionary that maps English terms to Emojis (broken into multiple lines for better readability).
```json
    {
        "happy": "😃",
        "heart": "😍",
        "rotfl": "🤣",
        "smile": "😊",
        "crying": "😭",
        "kiss": "😘",
        "clap": "👏",
        "grin": "😁",
        "fire": "🔥",
        "broken": "💔",
        "think": "🤔",
        "excited": "🤩",
        "boring": "🙄",
        "winking": "😉",
        "ok": "👌",
        "hug": "🤗",
        "cool": "😎",
        "angry": "😠",
        "python": "🐍"
    }
```

Use this dictionary to build a program that:

1. Reads a sentence from the user.
2. Replaces all the words in the sentence with the corresponding Emoji.

Below is an example execution of the program:
```text
    Please enter a sentence: I'm so excited to learn python
    I'm so 🤩 to finally learn 🐍
```
You should also be careful about spaces in the resulting sentence.

[Solution](./3.2/sol.py)
___
### Assignment

A [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) is a simple encryption technique. The encryption using a Ceasar cipher replaces a letter in the plain text with a letter that is a fixed number down in the alphabet. For example, with a shift of 5 the following substitutions would take place:

- a → f
- b → g
- c → h
- ...
- v → a
- w → b
- ...
- z → e

Using this substitutions, a plain text can be encrypted:

- Plaintext: programming python is fun!
- Encrypted text: uwtlwfrrnsl udymts nx kzs!

Your task for the assignment is to implement a Caesar cipher with a **shift of 5**. The program should ask the user for a plain text sentence and print the encrypted text.

Here is an example execution of the program:
```text
    Please enter a sentence: python is fun!
    The encrypted sentence is: udymts nx kzs!
```

Note that your program should not encrypt special characters like a space or an exclamation mark. If no substitution is defined for a character, the plain text character is used in the encryption as well (e.g. the *!* in the example above).

#### Hint

1. There are several approaches to solve this exercise. The simplest solution would be to create a dictionary containing the necessary substitutions.
2. To avoid handling upper and lower case letters it is best to first convert the user input to lower case. After that you only need to take into account lower case letters. A string can be converted into lower case using the .lower() method.

[Solution](./Assignment/sol.py)
___
### Assignment - Quiz

[Week 03 - Assignment Part-1 (Questions) Solutions](./quizAssg.md)

Note [⚠] <br>
Make sure to solve the quiz on your own. Refer the solutions only after solving the quiz.
___
### Bonus Assignment

The bonus exercise builds upon the assignment of this week. Here is the description of this weeks exercise again:

A [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) is a simple encryption technique. The encryption using a Ceasar cipher replaces a letter in the plain text with a letter that is a fixed number down in the alphabet. For example, with a shift of 5 the following substitutions would take place:

- a → f
- b → g
- c → h
- ...
- v → a
- w → b
- ...
- z → e


Using this substitutions, a plain text can be encrypted:

- Plaintext: programming python is fun!
- Encrypted text: uwtlwfrrnsl udymts nx kzs!

Your task for the bonus exercise is the implementation of a Caesar cipher with a variable shift. The program should ask the user for a number of characters for the shift first. Next the program should ask the user for a plain text sentence and print the encrypted text. Here is an example execution of the program:
```
    Please enter the number of places to shift: 5
    Please enter a sentence: python is fun!
    The encrypted sentence is: udymts nx kzs!
```
Here is another execution of the program:
```text
    Please enter the number of places to shift: 10
    Please enter a sentence: python is fun!
    The encrypted sentence is: zidryx sc pex!
```
And yet another one:
```text
    Please enter the number of places to shift: 0
    Please enter a sentence: python is fun!
    The encrypted sentence is: python is fun!
```

Your program should check that only numbers between 0 and 25 are entered for the number of places to shift!
```text
    Please enter the number of places to shift: 60
    You need to enter a number between 0 and 25!
```
[Solution](./Bonus/sol.py)
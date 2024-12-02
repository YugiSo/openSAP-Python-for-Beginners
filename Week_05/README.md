## Python for Begineers - Week 5

### Unit 2: Exercise

Implement a function named `get_student_data()`. The function should do the following:

- Using `input()` it asks for name, first name and a student-id.
- The values are packed into a tuple.
- This tuple is returned from the function

The function `get_student_data()` is then called in the program, the return value is assigned to a variable. Finally, output the variable using `print()`.

[Solution](./5.2/sol.py)
___
### Unit 3: Exercise

Implement the function `is_even(number)` which gets an integer as input parameter and checks, if this input is even or not. `is_even()` will return the boolean value `True` if the value is even and `False` if the input is not even.

Implement a `for` loop which iterates over the `range(100)`. Within the `for` loop, the sequence-variable is checked with the function `is_even()`. Depending on the return value, either `x is even` or `x is not even` is printed.

Example output:
```text
    0 is even
    1 is not even
    2 is even
    ...
```

[Solution](./5.3/sol.py)
___
### Unit 5: Exercise

The stopping distance of a car can be calculated using the following [rule of thumb](https://en.wikipedia.org/wiki/Braking_distance#Rules_of_thumb):

- The stopping distance of the car is the sum of the reaction path and the brake distance
- The reaction path depends on the speed. It can be calculated by the following rule of thumb: The reaction path in meter is equal to the speed in km/h times 3/10. - Example: Speed 50km/h --> reaction path 15m
- The brake distance depends as well on the speed. Again there is a rule of thumb which is: brake distance in m is equal to the speed in km/h divided by 10, the result has to be taken by the power of 2, Example: Speed 50km/h --> (50 / 10)\*\*2 = 25m
- The stopping distance for a car with a speed of 50km/h is 15m + 25m = 40m

#### Implement the following functions to calculate the stopping distance

- function `reaction_path()` which gets the speed in km/h as input, calculates the reaction path according to the above rule of thumb and returns the path in m.
- function `brake_distance()` which gets the speed in km/h as input, calculates the brake distance according to the above rule of thumb and returns the distance in m.
- function `stopping_distance()` which gets the speed in km/h as input, calls the above functions, adds their return values and returns this sum.

Get a speed in km/h as input and output the stopping distance in m.

[Solution](./5.5/sol.py)
___
### Assignment

You already implemented a solution for the [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) in week 3. As this cipher is quite weak, let's turn to another cipher, the [Vignère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher).

Like the Caesar cipher, the Vignère cipher is a simple substitution algorithm, that means, each letter is replaced by another letter. In the Caesar cipher, each letter is shifted the same number of times. And this number is the key. In Vignère these number of shifts change from letter to letter. The number of shifts are given by a keyword which is repeated until it matches the length of the text to be encrypted.

For simplification we assume, that only letters are encrypted and that we only have to deal with lower case letters. Let's have a look at the following example:

- In the first line there is the clear text.
- In the second line there is the repeated keyword `random`.
- In the third line the letter from the keyword is replaced by it's position in the alphabet (a: 0, b: 1, c: 2, ... z: 25). As `r` is on position 17, there is a 17 in the first position of the third row. This position determines how often the corresponding letter from the clear text has to be shifted.
- In the fourth line you can see the secret text. The first letter `p` from the clear text is shifted 17 times and results in `g` (as the end of the alphabet is already reached after 11 shifts, one starts again at the beginning of the alphabet). The second letter `y` is shifted 0 times as the `a` from `random` is at position 0 of the alphabet. Thus, this `y` is mapped to `y`. Important: The blank is not shifted as it is no letter. However the repetition of the keyword in line two is not influenced by that.

| &nbsp;      |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| Clear Text  | p   | y   | t   | h   | o   | n   |     | i   | s   |     | b   | e   | a   | u   | t   | i   | f   | u   | l   |
| Keyword     | r   | a   | n   | d   | o   | m   | r   | a   | n   | d   | o   | m   | r   | a   | n   | d   | o   | m   | r   |
| Position    | 17  | 0   | 13  | 3   | 14  | 12  | 17  | 0   | 13  | 3   | 14  | 12  | 17  | 0   | 13  | 3   | 14  | 12  | 17  |
| Secret Text | g   | y   | g   | k   | c   | z   |     | i   | f   |     | p   | q   | r   | u   | g   | l   | t   | g   | c   |

#### Your Task

Implement a program, that gets a text as input and in addition a keyword, which is
the number of shifts.

- Implement a function `encrypt_letter()`, that gets a character and the key as input. The return value will be the encrypted character.
- Implement a function `calculate_shifts()`, that gets a letter as input parameter and returns the position of this letter in the alphabet (starting with `a` at position 0):
- Implement a function `encrypt_text()`, that gets a text and a keyword as input and returns the encrypted text. This function calls both `calculate_shifts()`and `encrypt_letter()`


Below is an example output
```text
    Which text should be encrypted: Python is Really Beautiful
    Which keyword should be used? Random
    gygkcz if fqrlyb nvahwwrll
```

[Solution](./Assignment/sol.py)
___
### Assignment - Quiz

[Week 05 - Assignment Part-1 (Questions) Solutions](./quizAssg.md)

Note [⚠] <br>
Make sure to solve the quiz on your own. Refer the solutions only after solving the quiz.
___
### Bonus Assignment

[Prime numbers](https://en.wikipedia.org/wiki/Prime_number) are natural numbers greater than 1 which are not divisible by any number beside 1 and the number itself. In other words, the number cannot be composed as a product of two natural numbers other than 1 and the number itself. There are infinite prime numbers and the first ones are:

2, 3, 5, 7, 11, ...


Write a program, that gets an integer through input and creates a list containing all prime numbers until this input. To do so, two functions have to be implemented:

- The function `is_prime()` gets an integer as input and returns `True` if this integer is prime, and `False` if the integer is not prime.
- The function `prime_list()` gets an integer as input and checks each number from 2 to input, if it is prime by calling the above function. If a number is prime, it is appended to a list. This list is given back as the return value of `prime_list()`.

The program finally outputs the list of all prime numbers.
```text
Example 1:

    Up to which number do you want all prime numbers: 100
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

Example 2:

    Up to which number do you want all prime numbers: 13
    [2, 3, 5, 7, 11, 13]
```

[Solution](./Bonus/sol.py)
## Python for Begineers - Week 2

### Unit 2: Exercise

Below you find a code snippet to create a Python list containing the titles of all [Star Wars](https://en.wikipedia.org/wiki/Star_Wars) movies. The list contains:

- A list containing the titles of the prequel trilogy:
  _The Phantom Menace_, _Attack of the Clones_, _Revenge of the Sith_
- A list containing the titles of the original trilogy:
  _A New Hope_, _The Empire Strikes Back_, _Return of the Jedi_,
- A list containing the titles of the sequel trilogy:
  _The Force Awakens_, _The Last Jedi_, _The Rise of Skywalker_

```text
    star_wars_movies = [
        ["The Phantom Menace", "Attack of the Clones", "Revenge of the Sith"],
        ["A New Hope", "The Empire Strikes Back", "Return of the Jedi"],
        ["The Force Awakens", "The Last Jedi", "The Rise of Skywalker"],
    ]
```

Write a program that asks the user for a number of the trilogy (1, 2 or 3) and the number of the film in this trilogy (1, 2 or 3). Print the title of the film corresponding to the user selection.

[Solution](2.2/sol.py)
___
### Unit 4: Exercise

You are given the following list containing stock symbols, their current price as well as the absolute price change of the previous day:

```text
stocks = [["SAP", 106, -3.0], ["AAPL", 165, 1.25], ["TSLA", 860, 54.2], ["ORCL", 76, -0.25], ["ZM", 114, 6.2]]
```

As you plan to take some of the profits, write a program that creates a list of all the stock symbols with a change of more than +5 percent. The list should be named `sell_list`. The list should only contain the stock symbol, not the price or the absolute change. **Print the resulting list.**

[Solution](2.4/sol.py)
___
### Unit 5: Exercise

Write a program that lets the user input a two-dimensional
[matrix](<https://en.wikipedia.org/wiki/Matrix_(mathematics)>) (Hint: you could use a list of lists to store the
matrix). The program should first ask the user how many rows and columns the matrix should contain. Next, the program
should ask the user for the elements of the matrix. Your program should read the values from the user row by row. If,
for example, the matrix has the dimension 2 by 3, the values should be read as follows:

- First row, first value
- First row, second value
- First row, third value
- Second row, first value
- Second row, second value
- Second row, third value

Finally, the program should calculate and print the sums of the values in each row.

Below is an example execution of the program:
```text
    Please enter the number of rows in the matrix: 2
    Please enter the number of columns in the matrix: 3
    Enter the matrix values:
    Value: 1
    Value: 2
    Value: 3
    Value: 4
    Value: 5
    Value: 6
    Sum of row: 6
    Sum of row: 15
```

[Solution](./2.5/sol.py)
___
### Assignment - Code

In this exercise you are going to simulate a sales and operations planning using the [zero stock level](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/d853922bdd584e8e83027e5a0b8122f2/d06dbd534f22b44ce10000000a174cb4.html?locale=en-US)
strategy. Write a Python program that asks the user to enter the following data:

- An initial stock level for a product
- The number of month(s) to plan
- The planned sales quantity for each month

Based on this data, calculate the required production quantity as follows:

- If the sales quantity is smaller than the stock level of the previous month, the production quantity is 0
- If the sales quantity is larger than the stock level of the previous month, the production quantity is this difference

Below is an example execution of the program:
```text
    Please enter an initial stock level: 500
    Please enter the number of month to plan: 5
    Please enter the planned sales quantity: 300
    Please enter the planned sales quantity: 250
    Please enter the planned sales quantity: 200
    Please enter the planned sales quantity: 400
    Please enter the planned sales quantity: 100

    The resulting production quantities are:
    Production quantity month 1 - 0
    Production quantity month 2 - 50
    Production quantity month 3 - 200
    Production quantity month 4 - 400
    Production quantity month 5 - 100
```

Why are those production quantities calculated? The initial stock level is 500. In the first month 300 pieces are sold. Therefore, nothing needs to be produced and the resulting stock is 200 (= 500 - 300).

In the second month 250 pieces are sold. The stock level after the previous month is 200. Therefore 50 pieces need to be produced. The resulting stock level is 0 (= 200 + 50 - 250).

In the third month 200 pieces are sold. The stock level after the previous month is 0. Therefore 200 pieces need to be produced. The resulting stock level is 0 (= 200 - 200).

[Solution](./Assignment/sol.py)
___
### Assignment - Quiz

[Week 02 - Assignment Part-2 (Questions) Solutions](./quizAssg.md)

Note [⚠] <br>
Make sure to solve the quiz on your own. Refer the solutions only after solving the quiz.
___
### Bonus Assignment

Write a Python program that prints the numbers from 1 to 100.
If the number is dividable by 3 print *Fizz*, if the number is dividable by 5 print *Buzz* instead of the number.
If the number is dividable by 3 and 5 print *FizzBuzz*.

Below is the output of the program for the first 15 numbers:
```text
    1
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz
    11
    Fizz
    13
    14
    FizzBuzz
```
Can you use a list comprehension to solve this exercise? [Solution (List Comprehension)](./Bonus/alt_sol)

[Solution](./Bonus/sol.py)
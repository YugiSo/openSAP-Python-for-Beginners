## Python for Begineers - Week 4

### Unit 3: Exercise

The file `numbers.txt` contains random integer numbers. There is exactly one number per line. Read the file and output the three biggest numbers in the following form:
```text
	2345
	223
	89
```

[Solution](./4.3/sol.py)
___
### Unit 4: Exercise

The file `numbers.txt` contains numbers. (Actually, the same numbers from the last exercise.) There is exactly one number per line. Read the numbers from the file and write only the even numbers into a new file named `even_numbers.txt`. 

Again, there should be one number per line. The order of the numbers shall be unchanged. To indicate that the program is finished, print the following output: "List of even numbers created!"

[Solution](./4.4/sol.py)
___
### Unit 5: Exercise

The file *invoice_data.txt* contains raw data for an invoice. More precisely, each line contains

- the name of an item
- how many items are bought
- the unit price of the item

The three values are separated by a single whitespace. Prepare a beautified output of the file which contains

- the name of the item formatted with 15 characters
- the number of units with 3 digits
- the price per item with 7 digits, 2 digits after the decimal point
- the total price *(number of items * price per item)* with 8 digits in total, 2 digits after the decimal point

If there are two lines with the following content "Apple 5 0.99" and "Cherry 2 11.99", then the beautified output should look as follows:
```text
    Apple           15   0.99   14.85
    Cherry           2  11.99   23.98
```

#### Hint
Read the file line by line and create a list of tuples. Each tuple contains the item (`string`), the number of items (`integer`) the price per item (`float`). To identify the individual parts per line, use the method `.split()`. Prepare an `f-string` to output the data as specified.

[Solution](./4.5/sol.py)
___
### Assignment

There is a file `secret.txt`, which contains one character per line. There is a second file `key.txt`, which contains two lines with one number per line (the number could have several digits). The first number `col` represents the number of columns of a grid, the second number `row` represents the number of rows of the grid.

The characters of the first file should now be filled into this grid. Take the characters one by one and fill them into a string until the string contains `col` characters. Append the string to a list. Then create a new string the same way. Continue, until the number of strings is equal to `row`.  Now, write all the strings into a file `public.txt`. Open the
the file and check the content.


**Please note:**
When programming your solution in CodeOcean, files created by your program will not be visible. If you want to check the content of those files, we suggest to let your code run on your machine (e.g. in a Jupyter Notebook) and check the content of the files there.

#### Example

If the file `secret.txt` contains the following input:
```text
    #
    #
    #
    .
    #
    .
    .
    #
    .
    .
    #
    .
```

and the file `key.txt` contains the following numbers:
```text
    3
    4
```

then the content in the file `public.txt` should be as follows:
```text
    ###
    .#.
    .#.
    .#.
```

[Solution](./Assignment/sol.py)
___
### Assignment - Quiz

[Week 04 - Assignment Part-1 (Questions) Solutions](./quizAssg.md)

Note [⚠] <br>
Make sure to solve the quiz on your own. Refer the solutions only after solving the quiz.
___
### Bonus Assignment

You probably know the game ["Rock, Paper, Scissors"](https://en.wikipedia.org/wiki/Rock_paper_scissors). A game for two players. Each player has three options, namely rock, paper, scissors, which are formed by the player's hand. The rules are quite easy:

- rock beats scissors
- scissors beats paper
- paper beats rock.

If both players have chosen the same object, it's a draw.

In the following, we play 100 consecutive games. Each player has to hand in a file consisting of one letter per line. The letters are either "R", "P" or "S".

Write a Python program that reads two files `player1.txt` and `player2.txt`. These files are organized according to the above rules. The program should compare both inputs and calculate how many games have been won by player1, by player2 and how many games ended in a draw. The results are written into a file `result.txt` which looks as follows:
```text
	Player1 wins: 23
	Player2 wins: 48
	Draws: 29
```

The sum should always be 100.

[Solution](./Bonus/sol.py)
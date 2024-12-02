## Assignment Week 4 (Part 1 - Questions)

1. Which of the following statements about file handling in Python are correct? **(2.0 / 2.0)**
    > Note: There are 3 correct answers to this question.

    - [ ] Files must only contain the normal characters and digits.
    - [x] Using files, data can be stored persistently, in other words, when the program is stopped or when the computer is switched off, the data is still available.
    - [ ] The rules for naming a file are the same as the rules for naming variables.
    - [x] Files can be used to share data between different programs.
    - [x] Files must have a name, otherwise they are not "callable".

2. Which statements about the following code are correct? **(2.0 / 2.0)**

    ```py
    with open("first_file.txt", "r") as file:
        for line in file:
            print(line)
    ```

    > Note: There are 2 correct answers to this question.

    - [x] When a file is opened with the with statement, it is not necessary to close it. This is done automatically at the end of the with block.
    - [ ] The file will not be stored correctly at the end of the program because it is not closed correctly.
    - [ ] In this case, it does not matter that the .close() method is not executed, as the file is read only.
    - [x] Using the with statement in combination with the open function limits the number of faults, as the closing of the file is done implicitly.
    - [ ] Using the with statement, it does not matter if the file first_file.txt exists. In case there is no such file, the program will simply continue and does not raise an error.

3. Which statements regarding the following program are correct? **(2.0 / 2.0)**

    ```py
    with open("loren_ipsum.txt", "r") as file:
        line = file.readlines()
    ```

    > Note: There are 2 correct answers to this question.

    - [ ] The line breaks \n at the end of each line in the file are automatically deleted by the ‘with’ statement.
    - [ ] The file is not closed correctly at the end of the program.
    - [x] After the program is executed, the variable line is a list.
    - [ ] Only the first line of the file is read into the variable line.
    - [x] If the file "lorem_ipsum.txt" does not exist, the program stops with an error.

4. Which of the following statements about the .strip() method are correct? **(2.0 / 2.0)**

    > Note: There are 2 correct answers to this question.

    - [ ] If a file contains only digits, the .strip() method cannot be used, as it only works on strings.
    - [x] Using the string method .strip(), leading and ending spaces, tabs, line breaks, and so on, are deleted.
    - [ ] It is better to use the .strip() method multiple times (for example, string.strip().strip()), because then even double spaces are deleted.
    - [x] To loop through the lines of a file and first .strip() the line is a common pattern when dealing with files.
    - [ ] The method .lstrip() can be used on integers to delete leading zeros.

5. The following program is intended to write the numbers from 1 to 10 to a file. The numbers should be stored in subsequent lines. What mistakes does the program contain? **(2.0 / 2.0)**

    ```py
    with open("numbers.txt", w) as file:
        for i in range(1, 10):
            file.write(i + "\n")
    ```

    > Note: There are 3 correct answers to this question.

    - [ ] All data is written to one line and not to subsequent lines.
    - [ ] The mode "w+" has to be used because new data is stored into the file.
    - [x] The mode "w" has to be a string; the quotation marks are missing.
    - [x] The range has to be from 1 to 11 as the last value is not taken into account.
    - [x] The variable i has to be converted into a string.

6. What is the output of the following statements? **(1.0 / 1.0)**

    ```py
    print("Week 4", "Assignment", "Question 6", sep=" - ")
    ```

    - [ ] Week4 Assignment Question 6
    - [x] Week 4 – Assignment – Question 6
    - [ ] Week4–Assignment–Question 6
    - [ ] Week 4, Assignment, Question 6

7. What is the output of the following statements? **(1.0 / 1.0)**

    ```py
    print("Week 4", end=" - ")
    print("Assignment", end=" - ")
    print("Question 6", end=" - ")
    ```

    - [ ] Week 4
          Assignment
          Question 7
    - [ ] Week 4 – Assignment – Question 7
    - [x] Week 4 – Assignment – Question 7 –
    - [ ] Week 4 –
          Assignment –
          Question 7 –

8. What is the result of the following statement? **(1.0 / 1.0)**

    ```py
    print(f"4 * 3 = {4 * 3:10d}")
    ```

    - [ ] 4 * 3 = 1.2

    - [ ] 4 * 3 = 12

    - [x] 4 * 3 =         12

    - [ ] 4 * 3 = 12:10d

9. What is the result of the following statement? **(1.0 / 1.0)**

    ```py
    "John, Paul, George, Pete".replace("Pete", "Ringo")
    ```

    - [ ] John, Paul, George, Pete
    - [ ] Error
    - [ ] Ringo
    - [x] John, Paul, George, Ringo

10. What is the result of the following statement? **(1.0 / 1.0)**

    ```py
    "Yesterday, Let it be, Help, Something".split()
    ```

    - [ ] "Yesterday", "Let it be", "Help", "Something"
    - [x] ['Yesterday,', 'Let', 'it', 'be,', 'Help,', 'Something']
    - [ ] ['Yesterday', 'Let', 'it', 'be', 'Help', 'Something']
    - [ ] ['Yesterday', 'Let it be', 'Help', 'Something']
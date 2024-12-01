## Assignment Week 3 (Part 1 - Questions)

1. Which of the following statements about tuples are correct? **(2.0 / 2.0)**
    > Note: There are 3 correct answers to this question.

   - [x] Tuples are sequences. for loops can therefore be used to access each element of a tuple.
   - [ ] To add an element to a tuple, the method .append() can be used.
   - [ ] Tuples are represented by parenthesis ( ). Consequently, the index of the tuples uses parenthesis as well.
   - [x] The elements of a tuple can be accessed using an index.
   - [x] The elements within a tuple are ordered, but not necessarily sorted.

2. What is the value of variable a after the following statements have been executed? **(1.0 / 1.0)**

    ```py
    date = (2022, "April", 5)
    a = len(date)
    ```

   - [x] 3
   - [ ] 4
   - [ ] 10
   - [ ] 1

3. Which of the following statements about dictionaries are correct? **(2.0 / 2.0)**
    > Note: There are 2 correct answers to this question.

   - [x] Tuples can be used as a key in a dictionary.
   - [x] It is possible to loop over a dictionary with the for loop.
   - [ ] Lists can be used as a key in a dictionary.
   - [ ] If a key-value pair is added to a dictionary and the key already exists in this dictionary, an error occurs.
   - [ ] The output of the method .keys() has the data type list.

4. What is the value of the variable a after the following statements have been executed? **(1.0 / 1.0)**

    ```py
    tel = {"Peter":123, "Paul":456, "Mary":789}
    a = list(tel.keys())[1]
    ```

   - [x] Paul
   - [ ] Error
   - [ ] ("Paul", 456)
   - [ ] 456

5. Although lists, tuples, and dictionaries are all sequence types, there are a few differences between them. Which of the following statements about these data types is correct? **(2.0 / 2.0)**
    > Note: There are 3 correct answers to this question.

   - [x] The function len() can be used for lists, tuples, and dictionaries.
   - [x] Elements in lists and tuples are accessed by index, elements in dictionaries are accessed by key.
   - [x] A well suited combination of lists, tuples, and dictionaries (for example, a list of tuples) makes programs easier to implement.
   - [ ] List and tuples are immutable, dictionaries are not.
   - [ ] According to the recommendation in this unit, there should be just one data type used in a tuple.

6. What is the result of the following statements? **(1.0 / 1.0)**

    ```py
    studs = {(123, "Harry"), (234, "Hermoine"), (345, "Ron")}
    a = studs[123][1]
    ```

   - [ ] Index Error
   - [x] Syntax Error: Invalid Syntax
   - [ ] Harry is assigned to variable a.
   - [ ] Key Error

7. What is the value of variable a after the following statements have been executed? **(1.0 / 1.0)**

    ```py
    studs = {123: "Harry", 234: "Hermoine", 345: "Ron"}
    a = studs[1]
    ```

   - [ ] Index Error
   - [ ] 123 : Harry
   - [x] Key Error
   - [ ] "Harry"

8. What is the value of variable a after the following statements have been executed? **(1.0 / 1.0)**

    ```py
    studs = {123: "Harry", 234: "Hermoine", 345: "Ron"}
    if 1 in studs:
        a = studs[1]
    else:
        print("key does not exist")
    ```

   - [ ] (123 : "Harry")
   - [ ] (123, "Harry)
   - [ ] The variable a is undefined, because the program crashes.
   - [x] The variable a is undefined, because the program executes the else-part of the if-statement and the assignment of a is not executed (if there has been a value assigned to a before, this value is unchanged).

9. Which of the following statements about functions and methods for complex data types are correct? **(2.0 / 2.0)**
    > Note: There are 3 correct answers to this question.

   - [ ] The method .insert(i, x) can only be used for lists and tuples but not for dictionaries, because an index is required.
   - [x] The method .sort() cannot be used for tuples, because tuples are immutable.
   - [x] The function sorted() can be used for tuples, as the original tuple is unchanged. The function creates a new list.
   - [ ] If the method .keys() is used for lists, a list of all indices is given back.
   - [x] The functions min(), max(), and sorted() can only be used if the relation > is supported between all elements.

10. Which of the following statements about while loops are correct? **(2.0 / 2.0)**
    > Note: There are 3 correct answers to this question.

    - [ ] All while loops require a counter variable.
    - [ ] If the keyword break is reached, the loop is not exited directly. It is exited when the end of the conditional statements are reached the next time.
    - [x] while loops can be stopped by the keyword break.
    - [x] A while loop requires at least one statement, which is indented.
    - [x] You can nest for loops, while loops, and if statements.
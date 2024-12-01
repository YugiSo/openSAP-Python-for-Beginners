## Assignment Week 2 (Part 1 - Questions)

1. Which of the following statements about lists are correct? **(2.0 / 2.0)**
    > Note: There are 3 correct answers to this question.

   - [x] Lists can be empty, in other words, they contain no elements.
   - [x] Lists consist of several elements or items.
   - [ ] The elements within a list are always sorted by size.
   - [x] It is possible to add two lists. The result will again be a list.
   - [ ] You can multiply two lists. The result will be a list.

2. What is the content of variable list1 after the following statements have been executed? **(1.0 / 1.0)**

    ```py
    list1 = []
    list1 *= 3
    ```

   - [ ] [[[]]]
   - [ ] [] [] []
   - [ ] [3]
   - [x] []

3. Which of the following statements about indices are correct? **(2.0 / 2.0)**
    > Note: There are 3 correct answers to this question.

   - [x] Indices can be positive and negative.
   - [ ] For each element in the list, there is exactly one index.
   - [x] Indices are always of data type integer.
   - [x] Using an index bigger than the length of the list leads to an error.
   - [ ] The index -0 is not defined.

4. Which of the following statements about functions and methods for lists are correct? **(2.0 / 2.0)**
    > Note: There are 2 correct answers to this question.

   - [x] The method .append() adds a new item at the end of the list.
   - [ ] The function min() returns the smallest element of a list. If the list contains elements of different data types, an automatic casting of the data types takes place for all elements.
   - [x] The function len() returns the length of the list, that is, the number of elements the list contains.
   - [ ] The method .pop() returns the last element of a list. The list remains unchanged.
   - [ ] The method .remove() deletes all occurrences of the parameter in the parentheses contained in the list.

5. What is the value of the variable x after the following statements have been executed? **(1.0 / 1.0)**

    ```py
    x = 1
    list1 = [1, 2, 3, 4]
    for i in list1:
        x *= i
    ```

   - [ ] 1
   - [x] 24
   - [ ] 4
   - [ ] 10

6. Which of the following statements about loops are true? **(2.0 / 2.0)**
    > Note: There are 3 correct answers to this question.

   - [x] In each iteration of the for loop, the next element of the sequence is assigned to the sequence variable.
   - [ ] Because strings are not sequences, for loops cannot iterate over strings.
   - [x] for loops are well suited to iterate over sequences.
   - [x] for loops and if-elif-else constructs can be combined.
   - [ ] for loops iterating over an empty sequence (for example, an empty list) will result in an error.

7. Which of the following statements about ranges are correct? **(2.0 / 2.0)**
    > Note: There are 2 correct answers to this question.

   - [x] The first parameter of the range is the starting point of the created sequence, the second parameter is its endpoint. The first parameter belongs to the sequence, the second parameter does not.
   - [ ] Using a range, a sequence of characters can be created.
   - [x] Using a range, a sequence of numbers can be created.
   - [ ] If the second parameter of the range is negative, the created sequence is decreasing.
   - [ ] Ranges create sequences of integers. These sequences can be in increasing, in decreasing, or in an arbitrary order.

8. Which sequence is created by the following range? range(10, 1) **(1.0 / 1.0)**

   - [ ] Error
   - [ ] 10, 9, 8, 7, 6, 5, 4, 3, 2
   - [x] Empty sequence: there is no integer in the sequence
   - [ ] 9, 8, 7, 6, 5, 4, 3, 2, 1

9. What is the value of variable list2 after the following statements have been executed? **(1.0 / 1.0)**

    ```py
    list1 = list(range(5))
    list2 = [x for x in list1 if x % 2 == 0]
    ```

   - [ ] [0, 0.5, 1, 1.5, 2]
   - [ ] [0, 1, 2, 3, 4]
   - [ ] [1, 3]
   - [x] [0, 2, 4]

10. What is the value of list2 after the following statements have been executed? **(1.0 / 1.0)**
    
    ```py
    champions_league_winner = [["Liverpool FC", 6], ["Chelsea FC", 2],  ["Manchester City", 0]]
    list2 = [x[0] for x in champions_league_winner if x[1] > 0]
    ```

    - [ ] [ ]
    - [ ] [6, 2]
    - [x] ['Liverpool FC', 'Chelsea FC']
    - [ ] [ ['Liverpool FC', 6], ['Chelsea FC', 2] ]
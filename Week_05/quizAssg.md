## Assignment Week 5 (Part 1 - Questions)

1. Which of the following statements about functions are correct? **(2.0 / 2.0)**
    > Note: There are 3 correct answers to this question.

    - [x] Functions should have a name that supports the understanding of the functionality of this function.
    - [ ] In programming, functions are assignments of one set (E) to another set (D).
    - [x] In Python, a function is executed by simply calling the name of the function.
    - [x] If a function is called, it is not necessary to know the implementation details of this function.
    - [ ] Business functions like controlling and marketing are based on the definition of functions in programming.

2. Which of the following statements about return values in functions are correct? **(2.0 / 2.0)**

    > Note: There are 3 correct answers to this question.

    - [x] If the return statement within a function is executed, the function is terminated. That means, if there are more statements behind the return, these are not executed.
    - [ ] Functions must have at least one return statement.
    - [ ] The return values are limited to primitive data types.
    - [x] If a return value is an expression (for example, return 2 + 3) , then the expression is first calculated, and the result is given back.
    - [x] Functions can have several return statements.

3. What is the output of the following program? **(1.0 / 1.0)**

    ```py
    def f4():
        print(4)
        return 3
    print(f4() + f4())
    ```


    - [ ] 4
          8

    - [ ] 4
          6

    - [x] 4
          4
          6


    - [ ] 4
          6
          6

4. Which of the following statements about functions in Python are correct? **(2.0 / 2.0)**

    > Note: There are 3 correct answers to this question.

    - [x] If all parameters have a default value, then the function can be called without passing a parameter.
    - [x] Parameters can have default values, that means, if no value is passed, then the default value is taken instead.
    - [x] In the definition statement of the function, the parameters without default values must be listed before the parameters with default values.
    - [ ] If a parameter is not used within the function (no write or read access), an error is triggered.
    - [ ] If a parameter is declared without a default value and a function call does not pass a value to this parameter, then a random value is taken instead".

5. What is the outcome of the following program? **(1.0 / 1.0)**

    ```py
    def f2(x = 5):
        print(x)
        x += 1
        return x + 1
    
    print(f2(1) + f2())
    ```


    - [ ] 5
          5
          10

    - [ ] 1
          5
          8

    - [ ] 5
          5
          14

    - [x] 1
          5
          10


6. What is the outcome of the following program? **(1.0 / 1.0)**

    ```py
    def f3():
        x = 10
        print(x)
    
    x = 3
    f3()
    print(x + 1)
    ```


    - [ ] 3
          4

    - [ ] VariableMismatchError

    - [ ] 10
          11

    - [x] 10
          4


7. Which of the following statements about combining functions is correct? **(2.0 / 2.0)**

    > Note: There are 3 correct answers to this question.

    - [ ] It is not possible to call functions within the statement block of another function.
    - [x] Functions can be nested. They are executed from the inside out.
    - [ ] It is possible to combine functions by putting several functions into one expression (for example, f1() + f2()). However, it is not possible to include one function within another.
    - [x] Nesting functions should be done with care. Too much nesting can decrease the readability of a program.
    - [x] If functions are nested, the output of the inner function must fit to the expected input of the outer function.

8. What is the output of the following function? **(1.0 / 1.0)**

    ```py
    light_on = True

    def switch_light(x):
        return not x

    def print_light_state(light):
        if light:
            print("Light is on")
        else:
            print("Light is off")

    print_light_state(switch_light(switch_light(light_on)))
    ```

    - [x] Light is on
    - [ ] Light is off
    - [ ] False
    - [ ] True

9. Which of the following statements about destructuring is correct? **(2.0 / 2.0)**

    > Note: There are 2 correct answers to this question.

    - [ ] If several values are given behind the keyword return, the TooManyValuesError is triggered.
    - [x] There can be only one object returned back by a function.
    - [x] If several values are given behind the keyword return, these values are automatically packed into a tuple.
    - [ ] If several values are given behind the keyword return, they must have the same data type.
    - [ ] The values listed behind the keyword return must have a primitive data type.

10. What is the value of the variable j after the execution of the following statement? **(1.0 / 1.0)**

    ```py
    x = (1, 2, 3, 4, 5)
    _, i, *j = x
    ```

    - [ ] Error
    - [ ] 5
    - [ ] (3, 4, 5)
    - [x] [3, 4, 5]
## Python for Begineers - Week 1

### Unit 3: Exercise

Write a Python program that asks the user to enter:

- A name
- A start city
- A destination city and
- A means of transportation

The program should then print that the _name_ wants to travel from _start_ to _destination_ by _means of transportation_.

Below is an example execution of the program:
```text
    Please enter a name: Christian
    Please enter a start: Aachen
    Please enter a destination: Berlin
    Please enter a means of transportation: Train

    Christian wants to travel from Aachen to Berlin by Train
```

[Solution](1.3/sol.py)
___
### Unit 5: Exercise

Write a Python program that asks the user to enter three integer numbers. The program should output the largest of the three numbers.

Below is an example execution of the program:
```text
    Please enter the first number: 23
    Please enter the second number: 42
    Please enter the third number: 11

    The largest number is 42
```

[Solution](1.5/sol.py)
___
### Assignment - Code

[Triangles](https://en.wikipedia.org/wiki/Triangle#Types_of_triangle) can be classified based on their angles.

- A right triangle has one angle of 90°
- A obtuse triangle has one angle of more than 90°
- A triangle is acute if all three angles are less than 90°

Write a program that asks the user for the values of three angles in degrees. First check if the entered values are valid. The values are only valid if they are >0 and if their sum is 180°. If the entered values are valid, classify the triangle as right, acute or obtuse.

Below are two example executions of the program with invalid values:
```text
    Please enter the first angle: 60
    Please enter the second angle: 60
    Please enter the third angle: 100
    The entered values are not valid.

    Please enter the first angle: 200
    Please enter the second angle: -10
    Please enter the third angle: -10
    Angles smaller than 0 are not valid.
```

Here is another example execution of the program:
```text
    Please enter the first angle: 60
    Please enter the second angle: 30
    Please enter the third angle: 90
    The triangle is a right triangle.
```

[Solution](./Assignment/sol.py)
___
### Assignment - Quiz

[Week 01 - Assignment Part-1 (Questions) Solutions](./quizAssg.md)

Note [⚠] <br>
Make sure to solve the quiz on your own. Refer the solutions only after solving the quiz.
___
### Bonus Assignment

A [quadratic equation](https://en.wikipedia.org/wiki/Quadratic_equation) is an equation that can be written as

$$ ax^2 + bx + c = 0 $$

In this equation *x* represents an unknown number, and *a*, *b*, and *c* are representing known numbers.
Possible solutions for a given quadratic equation can be calculated by the formula

$$ x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$

The expression $$b^2 - 4ac$$

is called the [discriminant](https://en.wikipedia.org/wiki/Quadratic_equation#Discriminant).
Using the discriminant makes it is easy to check the number of solutions for a given quadratic equation:

- If the discriminant is 0, the quadratic equation has exactly one real solution.
- If the discriminant is > 0, the quadratic equation has two real solutions.
- If the discriminant is < 0, the quadratic equation has two complex solutions.

Write a program that asks the user for the numbers *a*, *b* and *c*. The program should then print out how many solutions the quadratic equation has.

Below is an example execution of the program:
```text
    Please enter the value of a: 4
    Please enter the value of b: 2
    Please enter the value of c: -2

    The quadratic equation has 2 real solutions.

    Please enter the value of a: 1
    Please enter the value of b: 2
    Please enter the value of c: 3

    The quadratic equation has 2 complex solutions.

    Please enter the value of a: 1
    Please enter the value of b: 2
    Please enter the value of c: 1

    The quadratic equation has 1 real solution.
```

[Solution](./Bonus/sol.py)
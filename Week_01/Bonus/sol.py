# Week 1 - Bonus Assignment

a = int(input("Please enter the value of a: "))
b = int(input("Please enter the value of b: "))
c = int(input("Please enter the value of c: "))

disc = b ** 2 - (4*a*c)

if disc == 0:
    print("The quadratic equation has 1 real solution.")
elif disc < 0:
    print("The quadratic equation has 2 complex solutions.")
else:
    print("The quadratic equation has 2 real solutions.")
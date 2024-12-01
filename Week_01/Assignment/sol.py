# Week 1 - Final Assignment

a = int(input("Please enter the first angle: "))
b = int(input("Please enter the second angle: "))
c = int(input("Please enter the third angle: "))

if (a + b + c) == 180:
    
    if a <= 0 or b <= 0 or c <= 0:
        print("Angles smaller than 0 are not valid.")
    elif a == 90 or b == 90 or c == 0:
        print("The triangle is a right triangle.")
    elif a > 90 or b > 90 or c > 90:
        print("The triangle is an obtuse triangle.")
    else:
        print("The triangle is an acute triangle.")

else:
    print("The entered values are not valid.")
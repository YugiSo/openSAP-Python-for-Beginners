# Week 1 - Unit 5: Exercise 

a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))
c = int(input("Please enter the third number: "))

max = a if a > b else b

if max < c:
   max = c

print(f"The largest number is {max}")
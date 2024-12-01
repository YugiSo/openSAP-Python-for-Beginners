# Week 2 - Bonus Assignment

res = []

for i in range(1, 101):
    if i % 3 == 0:
        if i % 5 == 0:
            res.append('FizzBuzz')
        else:
            res.append('Fizz')
    elif i % 5 == 0:
        res.append('Buzz')
    else:
        res.append(i)

for ele in res:
    print(ele)
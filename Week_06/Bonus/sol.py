# Week 6 - Bonus Assignment

from math import pi as truePI
from random import random

def getExpPI() -> float:
    
    inside = 0
    for _ in range(10000):
        x, y = random(), random()

        if (x*x + y*y) <= 1:
            inside += 1

    return 4 * (inside / 10000)

expPI = getExpPI()

print(f'Calculated value of π: {expPI}')
print(f'Value of π from math library: {truePI}')
print(f'Difference: {expPI - truePI}')
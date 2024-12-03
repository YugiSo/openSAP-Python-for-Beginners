# Week 6 - Unit 3: Exercise

from random import gauss
from statistics import mean, stdev

def GaussDistribution() -> list:
    return [gauss(100, 10) for _ in range(1000)]


res = GaussDistribution()

print(f'Mean: {mean(res)}')
print(f'Standard Deviation: {stdev(res)}')
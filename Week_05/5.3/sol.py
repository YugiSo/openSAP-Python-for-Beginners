# Week 5 - Unit 3: Exercise

def is_even(num):
    return num % 2 == 0
    
for i in range(100):
    print(f'{i} is even' if is_even(i) else f'{i} is not even') 
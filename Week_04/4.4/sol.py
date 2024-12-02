# Week 4 - Unit 4: Exercise

with open('Week_04/4.4/numbers.txt','r') as file:
    data = file.read()

data = data.strip('\n')   
data = [int(x) for x in data.split()]

even_num = [x for x in data if x % 2 == 0]

with open('Week_04/4.4/even_numbers.txt', 'w') as file:
    for num in even_num:
        num = f'{num}\n'
        file.write(num)

print(f'List of even numbers created!')
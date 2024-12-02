# Week 4 - Unit 5: Exercise

with open('Week_04/4.5/invoice_data.txt') as file:
    data = file.readlines()

items = []
for line in data:
    line = tuple(line.strip('\n').split(' '))
    items.append(line)

for item in items:
    unit, price = int(item[1]), float(item[2])
    
    print(f'{item[0]:<15}{unit:>3}{price:>7.2f}{unit * price:>8.2f}')
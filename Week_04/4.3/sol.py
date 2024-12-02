# Week 4 - Unit 3: Exercise

with open('Week_04/4.3/numbers.txt') as file:
    data = file.read()
    for line in data:
        line = line.strip('\n')

nums = [int(x) for x in data.split()]
nums.sort(reverse=True)

print(f'{nums[0]}\n{nums[1]}\n{nums[2]}')
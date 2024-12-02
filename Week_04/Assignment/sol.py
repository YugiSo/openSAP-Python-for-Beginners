# Week 4 - Assignment

with open("Week_04/Assignment/key.txt") as file:
    dims = file.read()
    col, row = [int(x) for x in dims.strip('\n').split()]

with open("Week_04/Assignment/secret.txt") as file:
    data = file.read()
    data = data.strip('\n').split()

public_data = []
for i in range(row):
    tmp = ''
    for j in range(col):
        tmp += data[j]
    
    data = data[col:]
    public_data.append(tmp)

# print(public_data)

with open("Week_04/Assignment/public.txt", 'w') as out:
    for sen in public_data:
        out.write(f'{sen}\n')
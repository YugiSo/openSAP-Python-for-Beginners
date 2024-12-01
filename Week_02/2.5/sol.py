# Week 5: Exercise

row = int(input("Please enter the number of rows in the matrix: "))
col = int(input("Please enter the number of columns in the matrix: "))

print("Enter the matrix values: ")

matrix = []

# '_' as I have no use of the variable
for _ in range(row):
    some_row = []
    for _ in range(col):
        ele = int(input("Value: "))
        some_row.append(ele)
        
    matrix.append(some_row)
    
for row in matrix:
    print(f'Sum of row: {sum(row)}')
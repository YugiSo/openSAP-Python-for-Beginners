# Week 2 - Final Assignment

ini_lvl = int(input("Please enter an initial stock level: "))
months = int(input("Please enter the number of month to plan: "))

sales = [ini_lvl]
temp = None

for i in range(months):
    temp = int(input("Please enter the planned sales quantity: "))
    sales.append(temp)

print("\nThe resulting production quantities are:\n")

# Main Logic

for i in range(months):
    if sales[1] < sales[0]:
        print(f'Production quantity month {i + 1} - 0')
        sales[0] = sales[0] - sales[1]
        sales.remove(sales[1])
        continue
    
    if (sales[1] > sales[0]):
        print(f'Production quantity month {i + 1} - {sales[1] - sales[0]}')
        sales[0] = 0
        sales.remove(sales[1])
        continue
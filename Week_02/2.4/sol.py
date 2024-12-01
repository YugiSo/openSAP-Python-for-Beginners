# Week 4: Exercise

stocks = [["SAP", 106, -3.0], ["AAPL", 165, 1.25], ["TSLA", 860, 54.2], ["ORCL", 76, -0.25], ["ZM", 114, 6.2]] 

sell_list = []

for st in stocks:
    if st[-1] > 5.0:
        sell_list.append(st[0])
        
print(sell_list)
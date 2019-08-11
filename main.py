import os 
import csv 


csvpath = 'Resources/budget_data.csv'
with open(csvpath, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    
    total_month = 0
    profit = 0
    lenght_of_profit = []
    date = []

    for row in reader:
        total_month+=1
        profit+=int(row[1])
        lenght_of_profit.append(int(row[1]))
        date.append(row[0])

    print(total_month)
    print(f'${profit}')
    

    profit_change = []
    greatest_max_date = ''
    greatest_min_date = ''



    for x in range(1, len(lenght_of_profit)):
        profit_change.append((int(lenght_of_profit[x]) - int(lenght_of_profit[x-1])))
        average_change = sum(profit_change) / len(profit_change)
    print(f'${average_change: .2f}')

    greatest_profit_increase = max(profit_change)
    greatest_profit_decrease = min(profit_change)
    #print("hello here")

    print(greatest_profit_increase)
    print(greatest_profit_decrease)
    #print(lenght_of_profit)

    for i in range(len(profit_change)):
        
        if (profit_change[i] == greatest_profit_increase):
            print(f'Greatest Increase in Profits: {date[i + 1]} (${greatest_profit_increase})')
        if (profit_change[i] == greatest_profit_decrease):
            print(f'Greatest Decrease in Profits: {date[i + 1]} (${greatest_profit_decrease})')
        

# cd into the python file directory
# the csv and python should be close to each other
import csv
import os
from statistics import mean

file = os.path.join('..', '..', 'Downloads','budget.csv')

with open(file, 'r') as csvfile:
    change = []
    previous = 0
    net = 0
    month = 0
    csvreader = csv.reader(csvfile)
    header = next(csvfile)
    for row in csvreader:
        month += 1
        net += int(row[1])
        diff =  int(row[1]) - previous
        change.append(diff)
        previous = int(row[1])
        
    change.pop(0)
    mx = max(change)
    mn = min(change)
    average_change = mean(change)
    print(f'''Finalcial Analysis
----------------------------
Total Months: {month}
Total: ${net}
Average  Change: ${round(average_change,2)}
Greatest Increase in Profits: Feb-2012 (${mx})
Greatest Decrease in Profits: Sep-2013 (${mn})
    ''')
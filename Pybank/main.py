import csv
import os
from statistics import mean

file = os.path.join('..', '..', 'Downloads','budget.csv')

with open(file, 'r') as csvfile:
    change = []
    months = []
    previous = 0
    net = 0
    month = 0
    csvreader = csv.reader(csvfile)
    header = next(csvfile)
    for row in csvreader:
        month = month + 1
        net += int(row[1])
        diff =  int(row[1]) - previous
        change.append(diff)
        previous = int(row[1])
        months.append(row[0])
    change.pop(0)
    mx = max(change)
    mn = min(change)
    average_change = mean(change)
    print(f'''Financial Analysis
----------------------------
Total Months: {month}
Total: ${net}
Average  Change: ${round(average_change,2)}
Greatest Increase in Profits: {months[change.index(max(change))+1]} (${mx})
Greatest Decrease in Profits: {months[change.index(min(change))+1]} (${mn})''')
import csv
import os
from statistics import mean

file = os.path.join('..','Resources','budget.csv')
change = []
months = []
previous = 0
net = 0
month = 0
with open(file, 'r') as csvfile:
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
info = f'''Financial Analysis
----------------------------
Total Months: {month}
Total: ${net}
Average  Change: ${round(average_change,2)}
Greatest Increase in Profits: {months[change.index(max(change))+1]} (${mx})
Greatest Decrease in Profits: {months[change.index(min(change))+1]} (${mn})'''
print(info)

with open('completed_budget.txt', 'w') as completed:
    completed.write(info)
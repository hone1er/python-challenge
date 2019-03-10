import csv
import os
from statistics import mean

data = os.path.join('..','Resources','budget.csv') 
change = []                         # list to store changes in value month to month
months = []                         # list of all months
previous = 0                        # profit/loss value of previous row
net = 0                             # net total for all rows
month = 0                           # month count
with open(data, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvfile)          # skip/store header
    for row in csvreader:
        month = month + 1                    # add 1 to month for each row to track total number of months
        net += int(row[1])                   # add the value in profit/loss column to net value
        diff =  int(row[1]) - previous       # get the difference between the current row and the previous row profit/loss
        change.append(diff)                  # append the diffence to the list 'change'
        previous = int(row[1])               # store the value in previous to use on the next iteration
        months.append(row[0])                # append the month to the months list
change.pop(0)               # remove the first index in the list otherwise mean(change) will be incorrect
mx = max(change)            # get the max and min of change
mn = min(change)
average_change = mean(change)       # get the average of change in profit/loss month to month
info = f'''Financial Analysis
----------------------------
Total Months: {month}
Total: ${net}
Average  Change: ${round(average_change,2)}
Greatest Increase in Profits: {months[change.index(max(change))+1]} (${mx})
Greatest Decrease in Profits: {months[change.index(min(change))+1]} (${mn})'''    # data stored in info to be printed and written to .txt file
print(info)

with open('completed_budget.txt', 'w') as completed:
    completed.write(info)
import csv
import os

file = os.path.join("..", "..", "Downloads","budget.csv")

with open(file, 'r') as csvfile:
    net = 0
    month = 0
    csvreader = csv.reader(csvfile)
    header = next(csvfile)
    for row in csvreader:
        month += 1
        net += int(row[1])


import csv
import os

file = os.path.join("..", "..", "Downloads","budget.csv")

with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvfile)
    net = 0
    for x in csvreader:
        net += int(x[1])

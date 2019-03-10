import csv
import os
import operator

data = os.path.join('..', 'Resources', 'election_data.csv')
vote_count = 0
khan = 0
correy = 0
li = 0
otooley = 0
with open(data, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvfile)
    for row in csvreader:
        vote_count +=1
        if row[2] == 'Khan':
            khan += 1
        elif row[2] == 'Correy':
            correy +=1
        elif row[2] == 'Li':
            li += 1
        elif row[2] == "O'Tooley":
            otooley +=1

percents = {'Khan': (khan/vote_count)*100, 'Correy': (correy/vote_count)*100, 'Li': (li/vote_count)*100, "O'Tooley": (otooley/vote_count)*100}
winner = max(percents.items(), key=operator.itemgetter(1))[0]
info = f"""
Election Results
-------------------------
Total Votes: {vote_count}
-------------------------
Khan: {round(percents['Khan'],3)}% ({khan})
Correy: {round(percents['Correy'],3)}% ({correy})
Li: {round(percents['Li'],3)}% ({li})
O'Tooley: {round(percents["O'Tooley"],3)}% ({otooley})
-------------------------
Winner: {winner}
-------------------------

"""
print(info)

with open('final_results.txt', 'w') as final:
    final.write(info)
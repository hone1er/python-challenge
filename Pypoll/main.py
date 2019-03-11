import csv
import os
import operator

data = os.path.join('..', 'Resources', 'election_data.csv')
vote_count = 0
votes = {'Khan': 0, 'Correy': 0, 'Li': 0, "O'Tooley": 0}
with open(data, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvfile)
    for row in csvreader:
        vote_count +=1
        if row[2] == 'Khan':
            votes['Khan'] += 1
        elif row[2] == 'Correy':
            votes['Correy'] +=1
        elif row[2] == 'Li':
            votes['Li'] += 1
        elif row[2] == "O'Tooley":
            votes["O'Tooley"] +=1
percents = {'Khan': (votes['Khan']/vote_count)*100, 'Correy': (votes['Correy']/vote_count)*100, 'Li': (votes['Li']/vote_count)*100, "O'Tooley": (votes["O'Tooley"]/vote_count)*100}
winner = max(votes.items(), key=operator.itemgetter(1))[0]
info = f"""
Election Results
-------------------------
Total Votes: {vote_count}
-------------------------
Khan: {round(percents['Khan'],3)}% ({votes['Khan']})
Correy: {round(percents['Correy'],3)}% ({votes['Correy']})
Li: {round(percents['Li'],3)}% ({votes['Li']})
O'Tooley: {round(percents["O'Tooley"],3)}% ({votes["O'Tooley"]})
-------------------------
Winner: {winner}
-------------------------

"""
print(info)

with open('final_results.txt', 'w') as final:
    final.write(info)
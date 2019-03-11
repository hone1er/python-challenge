import csv
import os
import operator
import timeit

data = os.path.join('..', 'Resources', 'election_data.csv')
vote_count = 0
# list of candidates. If a name is added to the csv, add it to this list.
candidates = ['Khan', 'Correy', 'Li', "O'Tooley"] 
# dictionary to store candidate: vote_count
votes = {}
with open(data, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvfile)
    for row in csvreader:
        vote_count +=1
        # check if candidate in votes dict, if the are, add 1 to their vote count, if not, add them to the dict with 1 vote
        if row[2] not in votes:
            votes[row[2]] = 1
        else:
            votes[row[2]] += 1
# create table of candidate stats
table = "\n".join([f"{name}: {round((votes[name]/vote_count)*100,3)}% ({format(votes[name], ',d')})" for name in candidates])
# get the max value in the votes dict and return the key
winner = max(votes.items(), key=operator.itemgetter(1))[0]
info = f"""
Election Results
-------------------------
Total Votes: {format(vote_count, ',d')}
-------------------------
{table}
-------------------------
Winner: {winner}
-------------------------
"""
print(info)
with open('final_results.txt', 'w') as final:
    final.write(info)
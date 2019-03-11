import csv
import os
import operator

data = os.path.join('..', 'Resources', 'election_data.csv')
vote_count = 0
# list of candidates(using this method allows you to add a name to the list of candidates)
candidates = ['Khan', 'Correy', 'Li', "O'Tooley"] 
# dictionary to store candidate: vote_count
votes = {}
# dictionary to store candidate: vote percentage
percent = {}
# fill votes dict using the list of candidates and set their votes to 0
for name in candidates:
    votes[name] = 0

with open(data, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvfile)
    for row in csvreader:
        vote_count +=1
        # check if candidate in votes dict, if the are, add 1 to their vote count
        if row[2] in votes:
            votes[row[2]] += 1
# populate the percent dict using a for loop through the candidate list and create table of candidate stats
table = ""
for name in candidates:
    percent[name] = (votes[name]/vote_count)*100
    table += (f"\n{name}: {round(percent[name],3)}% ({format(votes[name], ',d')})")
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
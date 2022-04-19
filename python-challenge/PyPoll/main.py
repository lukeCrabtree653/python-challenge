import csv
from lib2to3.pgen2.token import PERCENT
import os

csvpath = "Desktop/python-challenge/PyPoll/Resources/election_data.csv"

count = 0
name = ""
previousRow = ""
candidateNames = ["","",""]
candidateVotes = []
candidatePercent = []
voteCount1 = 0
voteCount2 = 0
voteCount3 = 0
i = 1
winner = ""

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # print(csv_header)
    for row in csvreader:
        if count == 0:
            name = row[2]
            candidateNames[0] = row[2]
        if row[2] not in candidateNames:
            candidateNames[i] = row[2]
            i = i + 1  
        count = count + 1
        previousRow = row[2]
        if row[2] == candidateNames[0]:
            voteCount1 = voteCount1 + 1 
        if row[2] == candidateNames[1]:
            voteCount2 = voteCount2 + 1
        if row[2] == candidateNames[2]:
            voteCount3 = voteCount3 + 1   

candidateVotes.append(voteCount1)
candidateVotes.append(voteCount2)
candidateVotes.append(voteCount3)

candidatePercent.append(voteCount1/count)
candidatePercent.append(voteCount2/count)
candidatePercent.append(voteCount3/count)

if voteCount1 > voteCount2 and voteCount1 >voteCount3:
    winner = candidateNames[0]
if voteCount2 > voteCount1 and voteCount2 > voteCount3:
    winner = candidateNames[1]
if voteCount3 > voteCount1 and voteCount3 > voteCount2:
    winner = candidateNames[2]

print("Election Results")
print("-------------------------")
print(f"Total Votes: {count}")
print("-------------------------")
for i in range(3):
    print(f"{candidateNames[i]}: {'{:.3%}'.format(candidatePercent[i])} ({candidateVotes[i]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")    


file = open("Desktop/python-challenge/PyPoll/analysis/analysis.txt","w")
file.write("Election Results")
file.write("\n")
file.write("-------------------------")
file.write("\n")
file.write(f"Total Votes: {count}")
file.write("\n")
file.write("-------------------------")
file.write("\n")
for i in range(3):
    file.write(f"{candidateNames[i]}: {'{:.3%}'.format(candidatePercent[i])} ({candidateVotes[i]})")
    file.write("\n")
file.write("-------------------------")
file.write("\n")
file.write(f"Winner: {winner}")
file.write("\n")
file.write("-------------------------")
file.close()
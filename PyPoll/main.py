import os
import csv
import math

#determine current directory and direct to the election file to read
cwd = os.getcwd()
csvpath = os.path.join(cwd,'Resources','election_data.csv')

#define the variables
current_counter = 0
total_vote_count = 0
candidate = ""
candidates_list = []
unique_candidates = {"Name":[],"Vote Count":[], "Percent of Votes": []}
vote_count = []
max_vote = "X"
max_vote_count = 0

#set dataset to go through with reader
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')

    #store header
    csv_header=next(csvreader)

    #loop through dataset to calculate
    for row in csvreader:
        candidates_list.append(row[2])
        
#count the candidates 
candidates_list = sorted(candidates_list)        
total_vote_count = len(candidates_list)

for row in candidates_list:
    if candidate != row:
        unique_candidates["Name"].append(row)
        count = candidates_list.count(row)
        unique_candidates["Vote Count"].append(count)
        unique_candidates["Percent of Votes"].append(round((count/total_vote_count*100),3))
        if count > max_vote_count:
            max_vote_count = count
            max_vote = row
    candidate = row

print(total_vote_count)
# winner = unique_candidates[unique_candidates.index(unique_candidates)]
print(max_vote)
print(unique_candidates)
    
#          vote_count.append(total_votes)
#          candidate = str(row[0])
#          unique_candidates.append(str(row[0]))
#          total_votes = 1
#     else: total_votes += 1

# print(vote_count)
# print(unique_candidates)    


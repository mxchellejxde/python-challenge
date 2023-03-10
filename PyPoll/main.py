import os
import csv

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
index = 0

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

#create a dictionary of the election results: name, vote count, percent of votes as keys and appending the values into the dictionary with every total result
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

#create output file and the results
output_file = os.path.join(cwd,"analysis","output.csv")
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    #write file for election results
    writer.writerow(["Election Results"])
    writer.writerow(["-------------------------"])
    #TERMINAL - print results to terminal
    print("Election Results")
    print("-------------------------")
    

    #write the total vote count
    writer.writerow(["Total Votes: "+str(total_vote_count)])
    writer.writerow(["-------------------------"])
    #TERMINAL - print total votes
    print("Total Votes: "+str(total_vote_count))
    print("-------------------------")

#iterate through the list of candidates and print/write the results of the election
    while index < len(unique_candidates["Name"]):
        name = unique_candidates["Name"][index]
        percent = str(unique_candidates["Percent of Votes"][index])
        vote = str(unique_candidates["Vote Count"][index])
        #write to CSV the list of candidates and the result of election
        writer.writerow([name
            + ": "
            + percent
            + "% ("
            + vote
            +")"])
        #TERMINAL - print the list of candidates and the result of election
        print(name
            + ": "
            + percent
            + "% ("
            + vote
            +")")
        index +=1
    #write the winner into the file
    writer.writerow(["-------------------------"])
    writer.writerow(["Winner: "+max_vote])
    writer.writerow(["-------------------------"])
    #TERMINAL - print the winner of the election into terminal
    print("-------------------------")
    print("Winner: "+max_vote)
    print("-------------------------")


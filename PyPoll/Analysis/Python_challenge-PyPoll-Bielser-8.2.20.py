#establish reference file
import os
import csv

election_csv = os.path.join("../Resources","election_data.csv")

#The total number of votes cast
with open(election_csv,"r",newline="") as election_file:

    #create csv reader
    csv_reader = csv.reader(election_file, delimiter=",")

    #create variables
    total_votes = 0
    candidate_dict = {}

    #skip header row
    csv_header = next(election_file)

    for row in csv_reader:
    
        #candidate name 
        candidate = row[2]

        #total votes cast
        total_votes = total_votes + 1

        #complete list of candidates who received votes
        if candidate in candidate_dict:
            candidate_dict[candidate] = candidate_dict[candidate] + 1
            
        else:
            #initailze value for new key
            candidate_dict[candidate] = 1
            
#The percentage of votes each candidate won
percentage_list = [
    candidate_dict["Khan"] / total_votes * 100,
    candidate_dict["Correy"] / total_votes * 100,
    candidate_dict["Li"] / total_votes * 100,
    candidate_dict["O'Tooley"] / total_votes * 100]

#The total number of votes each candidate won
total_votes_list = [
    candidate_dict["Khan"],
    candidate_dict["Correy"],
    candidate_dict["Li"],
    candidate_dict["O'Tooley"]]

#The winner of the election based on popular vote.
max_votecount = 0

for candidate,value in candidate_dict.items():
    if value > max_votecount:
        max_votecount = value
        winner = candidate

print(f'Election Results')
print(f'--------------------------------------')
print(f'Total Votes: {total_votes}')
print(f'--------------------------------------')
print(f'Khan: {percentage_list[0]:.3f}% ({total_votes_list[0]})')
print(f'Correy: {percentage_list[1]:.3f}% ({total_votes_list[1]})')
print(f'Li: {percentage_list[2]:.3f}% ({total_votes_list[2]})')
print(f'O\'Tooley: {percentage_list[3]:.3f}% ({total_votes_list[3]})')
print(f'--------------------------------------')
print(f'Winner: {winner}')
print(f'--------------------------------------')

#export text file
with open("PyPoll_Analysis.txt","w") as out_file:
    out_file.write(f"Election Results \n")
    out_file.write(f"-------------------------------------- \n")
    out_file.write(f'Total Votes: {total_votes}\n')
    out_file.write(f"-------------------------------------- \n")
    out_file.write(f'Khan: {percentage_list[0]:.3f}% ({total_votes_list[0]})\n')
    out_file.write(f'Correy: {percentage_list[1]:.3f}% ({total_votes_list[1]})\n')
    out_file.write(f'Li: {percentage_list[2]:.3f}% ({total_votes_list[2]})\n')
    out_file.write(f'O\'Tooley: {percentage_list[3]:.3f}% ({total_votes_list[3]})\n')
    out_file.write(f"-------------------------------------- \n")
    out_file.write(f'Winner: {winner}\n')
    out_file.write(f"-------------------------------------- \n")
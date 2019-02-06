#-------------------------#
# Holly Bergen            #
# 06Feb2019               #
# Election Analysis       #
#-------------------------#

import os
import csv

path = os.path.join(".", "PyPol", "election_data.csv")
with open(path, 'r') as csvfile:
    pollingreader = csv.reader(csvfile, delimiter = ',')

    #Label headers, save as variable
    header = next(pollingreader)

    #Assign columns
    voter_id = []
    country = []
    candidate =[]
    
    for row in pollingreader:
        
        voter_id.append(row[0])
        country.append(row[1])
        candidate.append(row[2])
    
#The total number of votes cast
    total_votes = (len(voter_id))

#A complete list of candidates who received votes
    candidate_list = list(set(candidate))
    
    #Correcting misspelled name in candidate list
    for n, i in enumerate(candidate):
        if i == 'Kh`n':
            candidate[n] = 'Khan'
            
#The total number of votes each candidate won

    #This loop saves counts for each candidate as its own variable
    counts = set(candidate)
    for name in counts:
        if name == "O'Tooley":
            otooley_count = (candidate.count(name))
        elif name == "Khan":
            khan_count = (candidate.count(name))
        elif name == "Li":
            li_count = (candidate.count(name))
        elif name == "Correy":
            correy_count = (candidate.count(name))

            
#The percentage of votes each candidate won. Calculated based on counts vs total votes
    
    otooley_perc = round(((otooley_count/total_votes)*100),3)
    khan_perc = round(((khan_count/total_votes)*100),3)
    li_perc = round(((li_count/total_votes)*100),3)
    correy_perc = round(((correy_count/total_votes)*100),3)
        

#The winner of the election based on popular vote.

    total_list = {'Khan': khan_count,'Correy': correy_count,'Li': li_count,'OTooley': otooley_count}
    winner = max(total_list, key=lambda key: total_list[key])
    #print(winner)


#-------------------------Print final results-------------------------#

print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
print(f'Khan: {khan_perc}% ({khan_count})')
print(f'Correy: {correy_perc}% ({correy_count})')
print(f'Li: {li_perc}% ({li_count})')
print(f'O\'Tooley: {otooley_perc}% ({otooley_count})')
print(f'-------------------------')
print(f'Winner: {winner}')
print(f'-------------------------')

#--------------------Print final results to text file-------------------#
with open("polling_text.txt", "a") as write_file:
    
    print(f'Election Results', file=write_file)
    print(f'-------------------------', file=write_file)
    print(f'Total Votes: {total_votes}', file=write_file)
    print(f'-------------------------', file=write_file)
    print(f'Khan: {khan_perc}% ({khan_count})', file=write_file)
    print(f'Correy: {correy_perc}% ({correy_count})', file=write_file)
    print(f'Li: {li_perc}% ({li_count})', file=write_file)
    print(f'O\'Tooley: {otooley_perc}% ({otooley_count})', file=write_file)
    print(f'-------------------------', file=write_file)
    print(f'Winner: {winner}', file=write_file)
    print(f'-------------------------', file=write_file)
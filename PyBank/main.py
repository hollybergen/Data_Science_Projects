#-------------------------#
# Holly Bergen            #
# 06Feb2019               #
# Budget Analysis         #
#-------------------------#

import os
import csv
import math

path = os.path.join('budget_data.csv')
with open(path, 'r') as csvfile:
    budgetreader = csv.reader(csvfile, delimiter = ',')
  
#Remove headers & first row and save as separate variable
    
    header = next(budgetreader)
    
#Assign column variable names and append using loop 

    months =[]
    profit_losses =[]
      
    for row in budgetreader:

        months.append(row[0])
        profit_losses.append(row[1])
        
#Calculate the number of months

    num_months = len(months)
    
#Calculate the net total amount of "Profit/Losses" over the entire period

    profit_losses = [int(x) for x in profit_losses]
    sum_pl = sum(profit_losses)


#--------------------------------In this loop---------------------------------#
#     The average of the changes in "Profit/Losses" over the entire period    #
#  The greatest increase in profits (date and amount) over the entire period  #
#  The greatest decrease in losses (date and amount) over the entire period   #
#-----------------------------------------------------------------------------#

    pl_change =[]

for row in range(1,len(profit_losses)):
    
    pl_change.append(profit_losses[row] - profit_losses[row-1])   
    
    avg_pl_change = sum(pl_change)/len(pl_change)
    max_pl_change = max(pl_change)
    min_pl_change = min(pl_change)
    max_pl_change_date = str(months[pl_change.index(max(pl_change))])
    min_pl_change_date = str(months[pl_change.index(min(pl_change))])


#---------------------------------Print final---------------------------------#
    
print("Financial Analysis")
print("-----------------------------------------------------")
print("Total Months:", num_months)
print("Total Revenue: $", sum_pl)
print("Avereage Revenue Change: $", math.ceil(avg_pl_change*100)/100)
print("Greatest Increase in Revenue:", max_pl_change_date,"($", max_pl_change,")")
print("Greatest Decrease in Revenue:", min_pl_change_date,"($", min_pl_change,")")


#---------------------------------write to text file---------------------------------#

with open("textfile_budget.txt", "a") as write_file:
    print(f"Financial Analysis", file=write_file)
    print(f"-----------------------------------------------------", file=write_file)
    print(f"Total Months:", num_months, file=write_file)
    print(f"Total Revenue: $", sum_pl, file=write_file)
    print(f"Avereage Revenue Change: $", math.ceil(avg_pl_change*100)/100, file=write_file)
    print(f"Greatest Increase in Revenue:", max_pl_change_date,"($", max_pl_change,")", file=write_file)
    print(f"Greatest Decrease in Revenue:", min_pl_change_date,"($", min_pl_change,")", file=write_file)

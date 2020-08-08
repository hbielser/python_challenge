#establish reference file
import os
import csv

budget_csv = os.path.join("../Resources","budget_data.csv")

#The total number of months included in the dataset
with open(budget_csv,"r", newline="") as budget_file:

    #create csv reader
    csv_reader = csv.reader(budget_file, delimiter=",")

    #set values
    total_months = 0
    total_prof_loss = 0.00
    prev_mo = 0.00
    Diff = 0
    DiffMax = 0
    DiffMin = 0

    #skip header row
    csv_header = next(budget_file)

    for i in csv_reader:
        #set month index
        month = i[0]
        #set prof_loss index
        prof_loss = i[1]
        #define prof_loss as integer
        iAmount = int(prof_loss)
        #define diff calculation
        Diff = iAmount - prev_mo

#The total number of months included in the dataset
        total_months = total_months + 1
        
        #The net total amount of "Profit/Losses" over the entire period
        total_prof_loss += iAmount

        #The average of the changes in "Profit/Losses" over the entire period
        avg_change = total_prof_loss / total_months

        #The greatest increase in profits (date and amount) over the entire period
        if DiffMax < Diff:
            DiffMax = Diff
            DiffMaxDate = month
    
        #The greatest decrease in losses (date and amount) over the entire period
        if DiffMin > Diff:
            DiffMin = Diff
            DiffMinDate = month    

        prev_mo = iAmount

    output_list = [
    print(f'Financial Analysis'),
    print(f'------------------------------------'),
    print(f'Total Months: {total_months}'),
    print(f'Total: ${total_prof_loss:.0f}'),
    print(f'Average Change: ${avg_change:.2f}'),
    print(f'Greatest Increase in Profits: {DiffMaxDate} (${DiffMax})'),
    print(f'Greatest Decrease in Profits: {DiffMinDate} (${DiffMin})')]

#Write to text file
with open("PyBank_Analysis.txt","w") as out_file:
    out_file.write(f"Financial Analysis \n")
    out_file.write(f"------------------------------------\n")
    out_file.write(f"Total Months: {total_months}\n")
    out_file.write(f"Total: ${total_prof_loss:.0f}\n")
    out_file.write(f"Average Change: {avg_change:.2f}\n")
    out_file.write(f"Greatest Increase in Profits: {DiffMaxDate} (${DiffMax})\n")
    out_file.write(f"Greatest Decrease in Profits: {DiffMinDate} (${DiffMin})\n")
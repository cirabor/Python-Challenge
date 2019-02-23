import os
import csv

# getting the csv file data set
csvFile = os.path.join("..","LearnPython","budget_data.csv")

# Create a variable to store the data file
csvDataset = []

# Creating a variable to store the dates
csvDataset_Month = []

# Creating a variable to store the Profit and Losses
csvDataset_Amount = []

# Creating line separator for summary output
lines = "-" * 45

# Read the file for each row of data and add it to csvdataset
with open(csvFile,'r') as bankFile:
    csvRead = csv.reader(bankFile,delimiter=',')
    # print(csvRead)
    csv_header = next(csvRead)
    #print(f"CSV Header: {csv_header}")
    for row in csvRead:
        # print(row)
        csvDataset.append(row)
        # adding the row content to the list
        csvDataset_Month.append(row)
        csvDataset_Amount.append(int(row[1]))

        # Total number of Months
        total_months = len(csvDataset_Month)

        # The Total net amount of the profit or loss
        net_total = 0
        for month, amount in csvDataset:
            net_total += int(amount)

        # Average change in profit or loss
        chgAmt = 0
        monthChg = []
        for amount in range(1,len(csvDataset_Amount)):
            # Subtracting the amount here
            monthChg.append(csvDataset_Amount[amount] - csvDataset_Amount[amount -1])
            chgAmt = round(sum(monthChg) / len(monthChg),2)
            # print(str(chgAmt))
            #loss date and amount over time
            for amount in range(1,len(csvDataset_Amount)):
                maxIncr = max(monthChg)
                maxIncrIndex = monthChg.index(maxIncr)
                maxDecr = min(monthChg)
                maxDecrIndex = monthChg.index(maxDecr)
                monthMaxIncr = csvDataset_Month[maxIncrIndex + 1]
                monthMaxDecr = csvDataset_Month[maxDecrIndex + 1]


# lets print out the output
print("Profit and Loss Financial Analysis")
print(f"{lines}")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${chgAmt}")
print(f"Greatest Increase in Profits: {monthMaxIncr} (${maxIncr})")
print(f"Greatest Decrease in Profit: {monthMaxDecr} (${maxDecr})")

# write to a text file
target = open("pyBank.txt", 'w')
target.write("Profit and Loss Financial Analysis\n")
target.write(f"{lines}\n") 
target.write(f"Total Months: {total_months}\n")
target.write(f"Total: ${net_total}\n")
target.write(f"Average Change: ${chgAmt}\n")
target.write(f"Greatest Increase in Profits: {monthMaxIncr} (${maxIncr})\n")
target.write(f"Greatest Decrease in Profits: {monthMaxDecr} (${maxDecr})\n")

  

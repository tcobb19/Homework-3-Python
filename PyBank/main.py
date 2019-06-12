import os
import csv

# read from csv file

bank_csv = os.path.join(".", "budget_data.csv")

#create variables and dictionaries to store best and worst months

months = 0
total = 0
best_month = {"month": "0", "profit": 0}
worst_month = {"month": "0", "loss": 0}

#open csv file

with open(bank_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        # count total number of months in column A    
        months += 1
        # determine sum of column B, net total profit / loss
        total += int(row[1])
        # record month with greatest profit
        if best_month["profit"] < int(row[1]):
            best_month["profit"] = int(row[1])
            best_month["month"] = row[0]
        # record month with greatest losses
        if worst_month["loss"] > int(row[1]):
            worst_month["loss"] = int(row[1])
            worst_month["month"] = row[0]
        
# determine average change per month
average = round(total / months, 2)
#print results to terminal
print("Financial Analysis \n ----------------")
print("Total months: " + str(months))
print("Total: " + str(total))
print("Average monthly change: " + str(average))
print("Greatest Increase in Profits: " + best_month["month"] + " " +  str(best_month["profit"]))
print("Greatest Decrease in Profits: " + worst_month["month"] + " " + str(worst_month["loss"]))

# export results to text file

result = open("analysis.txt", "w")
result.write("Financial Analysis \n ---------------- \n")
result.write("Total months: " + str(months) + "\n")
result.write("Total: " + str(total) + "\n")
result.write("Average monthly change: " + str(average) + "\n")
result.write("Greatest Increase in Profits: " + best_month["month"] + " " +  str(best_month["profit"]) + "\n")
result.write("Greatest Decrease in Profits: " + worst_month["month"] + " " + str(worst_month["loss"]))
result.close()
import os
import csv
#create filepath for csv data
poll_csv = os.path.join(".", "election_data.csv")

#initialize variables for vote counts for each candidate & total
allvote = 0
khan = 0
li = 0
tool = 0
correy = 0

#open csv file

with open(poll_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #count votes
    for row in csvreader:
        #count total votes
        allvote += 1
        #count votes for each candidate by incrementing their counter variable for each row where the candidate cell matches
        if row[2] == "Khan":
            khan += 1
        elif row[2] == "Correy":
            correy += 1
        elif row[2] == "Li":
            li += 1
        elif row[2] == "O'Tooley":
            tool += 1

#calculate percentage for each candidate
per_k = round(khan/allvote, 5)
per_c = round(correy/allvote, 5)
per_l = round(li/allvote, 5)
per_t = round(tool/allvote, 5)

#determine winner
if khan > correy and khan > li and khan > tool:
    winner = "Khan"
elif correy > khan and correy > li and correy > tool:
    winner = "Correy"
elif li > khan and li > correy and li > tool:
    winner = "Li"
else:
    winner = "O'Tooley"

#print results to terminal
print("Election Results \n-------------------------")
print("Total Votes: " + str(allvote))
print("-------------------------")
print("Khan: " + "{:.3%}".format(per_k) + " (" + str(khan) + ")")
print("Correy: " "{:.3%}".format(per_c) + " (" + str(correy) + ")")
print("Li: " + "{:.3%}".format(per_l) + " (" + str(li) + ")")
print("O'Tooley: " + "{:.3%}".format(per_t) + " (" + str(tool) + ")")
print("-------------------------")
print("Winner: " + winner)

#print results to .txt file

with open("results.txt", "w") as result:
    result.write("Election Results \n-------------------------")
    result.write("\nTotal Votes: " + str(allvote))
    result.write("\n-------------------------")
    result.write("\nKhan: " + "{:.3%}".format(per_k) + " (" + str(khan) + ")")
    result.write("\nCorrey: " "{:.3%}".format(per_c) + " (" + str(correy) + ")")
    result.write("\nLi: " + "{:.3%}".format(per_l) + " (" + str(li) + ")")
    result.write("\nO'Tooley: " + "{:.3%}".format(per_t) + " (" + str(tool) + ")")
    result.write("\n-------------------------")
    result.write("\nWinner: " + winner)
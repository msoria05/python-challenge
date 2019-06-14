# Unit 3 | Assignment - Py Me Up, Charlie
# PyPoll
#
# Modules
import os
import csv
#
# Set path for file
csvpath = os.path.join("../Resources", "election_data.csv")
#
# Open the CSV and get list of unique candidate names
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the first row of data (header)
    reader = csv.reader(csvfile)
    header_row = next(reader)
    # Create empty list to hold names of candidates
    unique_list = [] 
    for row in reader:
        if row[2] not in unique_list:
            unique_list.append(row[2]) 
#
# Open the CSV and calculate total votes and votes for each candidate
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the first row of data (header)
    reader = csv.reader(csvfile)
    header_row = next(reader)
    # Create variables to count total overall votes and total votes for each candidate
    total = 0
    total_count = 0
    candidate1_votes = 0
    candidate2_votes = 0
    candidate3_votes = 0
    candidate4_votes = 0
    # Loop through remaining rows
    for row in reader: 
        total += int(row[0])
        total_count = 1 + total_count
        if row[2] == unique_list[0]:
            candidate1_votes = 1 + candidate1_votes
        if row[2] == unique_list[1]:
            candidate2_votes = 1 + candidate2_votes
        if row[2] == unique_list[2]:
            candidate3_votes = 1 + candidate3_votes
        if row[2] == unique_list[3]:
            candidate4_votes = 1 + candidate4_votes
    # Calculate and format the percent of votes for each candidate
    candidate1_percent = (100 * float(candidate1_votes)/float(total_count))
    candidate2_percent = (100 * float(candidate2_votes)/float(total_count))
    candidate3_percent = (100 * float(candidate3_votes)/float(total_count))
    candidate4_percent = (100 * float(candidate4_votes)/float(total_count))
    # Determine winner by comparing percent votes for each
    WinnerTotal = 0
    if candidate4_percent > WinnerTotal:
        Winner = unique_list[3]
        WinnerTotal = candidate4_percent
    if candidate3_percent > WinnerTotal:
        Winner = unique_list[2]
        WinnerTotal = candidate3_percent
    if candidate2_percent > WinnerTotal:
        Winner = unique_list[1]
        WinnerTotal = candidate2_percent
    if candidate1_percent > WinnerTotal:
        Winner = unique_list[0]
        WinnerTotal = candidate1_percent
    # Print Election Results summary
    print(f"""
    Election Results
    --------------------- 
    Total Votes: {total_count}
    ---------------------
    {unique_list[0]}: {format(candidate1_percent, '.3f')}% ({candidate1_votes})
    {unique_list[1]}: {format(candidate2_percent, '.3f')}% ({candidate2_votes})
    {unique_list[2]}: {format(candidate3_percent, '.3f')}% ({candidate3_votes})
    {unique_list[3]}: {format(candidate4_percent, '.3f')}% ({candidate4_votes})
    --------------------- 
    Winner: {Winner}
    ---------------------""")
#
# Write results to text file
file = open("ElectionResults.txt", "w")
file.write("Election Results")
file.write("\n")
file.write("-------------------------")
file.write("\n")
file.write("Total Votes: " + str(total_count))  
file.write("\n")
file.write("-------------------------")
file.write("\n")
file.write(str(unique_list[0]) + " " + str(format(candidate1_percent, '.3f')) + "% (" + str(candidate1_votes) + ")")
file.write("\n")
file.write(str(unique_list[1]) + " " + str(format(candidate2_percent, '.3f')) + "% (" + str(candidate2_votes) + ")")
file.write("\n")
file.write(str(unique_list[2]) + " " + str(format(candidate3_percent, '.3f')) + "% (" + str(candidate3_votes) + ")")
file.write("\n")
file.write(str(unique_list[3]) + " " + str(format(candidate4_percent, '.3f')) + "% (" + str(candidate4_votes) + ")")
file.write("\n")
file.write("-------------------------")
file.write("\n")
file.write("Winner: " + Winner)
file.write("\n")
file.write("-------------------------")
file.close() 
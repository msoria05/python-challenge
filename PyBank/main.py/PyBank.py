# Unit 3 | Assignment - Py Me Up, Charlie
# PyBank
#
# Modules
import os
import csv
# Set path for file
csvpath = os.path.join("../Resources", "budget_data.csv")
# Open the CSV and create loop
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the first row (header)
    reader = csv.reader(csvfile)
    header_row = next(reader)
    # Read first row of data to set up initial values, which will be needed for change in profit/loss calculations 
    initial_row = next_row = next(reader)
    start_value = initial_row[1]
    # Set current and next values to intial values as placeholder, values will be updated in loop
    current_date = initial_row[0]
    current_value = initial_row[1]
    next_date = initial_row[0]
    next_value = initial_row[1]
    # Set up varaibles for total (profit/loss) and total count
    total = 0
    total_count = 0
    # Set up variables for calculating change in profit/loss, and sum of change values needed to calculate average
    change = 0.0
    sum_change = 0.0
    average_change = 0.0
    # Set up variables for greatest increase and decrease in change with corresponding date
    GreatestINcrease = 0
    GreatestINcrease_Date = initial_row[0]
    GreatestDEcrease = 0
    GreatestDEcrease_Date = initial_row[0]
    # Loop through remaining rows
    for row in reader:
        current_date = next_date
        current_value = next_value
        total = total + int(row[1])
        total_count = 1 + total_count
        next_date = row[0]
        next_value = row[1]
        change = int(next_value) - int(current_value)
        if GreatestINcrease < change:
            GreatestINcrease = change
            GreatestINcrease_Date = next_date
        if GreatestDEcrease > change:
            GreatestDEcrease = change
            GreatestDEcrease_Date = next_date
        sum_change = sum_change + float(change)   
    # Add initial values to total and total count that were not included in loop, and calculate average change
    total = int(start_value) + total
    average_change = float(sum_change) // float(total_count)
    total_count = total_count + 1
    # Print Financial Analysis summary
    print(f"""
    Financial Analysis
    ------------------ 
    Total Months: {total_count}
    Total: ${total}
    Average Change: ${format(average_change, '.2f')} 
    Greatest Increase in Profits: {GreatestINcrease_Date} (${GreatestINcrease})
    Greatest Decrease in Profits: {GreatestDEcrease_Date} (${GreatestDEcrease})""")
#
# Write results to text file
file = open("FinancialAnalysis.txt", "w")
file.write("Financial Analysis")
file.write("\n")
file.write("----------------------------")
file.write("\n")
file.write("Total Months: " + str(total_count))
file.write("\n")
file.write("Total: $" + str(total))
file.write("\n")
file.write("Average Change: $" + str(average_change))
file.write("\n")
file.write("Greatest Increase in Profits: " + str(GreatestINcrease_Date) + " ($" + str(GreatestINcrease)+ ")")
file.write("\n")
file.write("Greatest Decrease in Profits: " + str(GreatestDEcrease_Date) + " ($" + str(GreatestDEcrease)+ ")")
file.close()








    






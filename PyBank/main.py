# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("PyBank", "Resources", "budget_data.csv")

# Name variables and trackers
total_profit = 0
date_count = 0
net_change = 0
total_change = 0
greatest_inc = ["", 0]
greatest_dec = ["", 0]

# Open and read csv
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first
    csv_header = next(csvreader)
    # Set the rest of the data to a list
    csv_list = list(csvreader)
    # Find date total
    date_count = sum(1 for row in csv_list)
    print("Financial Analysis")
    print("----------------------------------------")
    print("Total Months:", date_count)

    # Find profit total
    for row in csv_list:
        total_profit += int(row[1])
    print("Total: $", total_profit)

# Reopen the csv to restart the reader
with open(csvpath, encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Read the header row
    budget_header = next(csv_reader)
    # Pull first row of actual numbers
    first_row = next(csv_reader)
    prev_net = int(first_row[1])
    # Track the net change
    for row in csv_reader:
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        total_change = total_change + net_change
        # Calculate the greatest increase
        if net_change > greatest_inc[1]:
            greatest_inc[0] = row[0]
            greatest_inc[1] = net_change
        # Calculate the greatest decrease
        if net_change < greatest_dec[1]:
            greatest_dec[0] = row[0]
            greatest_dec[1] = net_change
        avg_change = round(total_change/(date_count-1), 2)
    print("Average Change: $", avg_change)
    print("Greatest Increase in Profits:", greatest_inc)
    print("Greatest Decrease in Profits:", greatest_dec)

    # Export to .txt
    output_path = os.path.join("PyBank", "analysis", "results.txt")
    with open(output_path, 'a') as csvfile:
        # Initialize csv.writer
        csvwriter = csv.writer(csvfile, delimiter=" ")
        # Export the results
        csvwriter.writerow(["Financial Analysis"])
        csvwriter.writerow(["----------------------------------------"])
        csvwriter.writerow(["Total Months:", date_count])
        csvwriter.writerow(["Total Profit: $", total_profit])
        csvwriter.writerow(["Average Change: $", avg_change])
        csvwriter.writerow(["Greatest Increase in Profits:", greatest_inc])
        csvwriter.writerow(["Greatest Decrease in Profits:", greatest_dec])
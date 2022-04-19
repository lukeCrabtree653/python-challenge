import csv
import os
from tkinter import W

csvpath = "Desktop/python-challenge/PyBank/Resources/budget_data.csv"

monthCount = 0
totalPL = 0
previousRow = 0
change = 0
avgChange = 0
currentChange = 0
inc = 0
incDate = ""
dec = 0
decDate = ""


with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    #print(csv_header)
    for row in csvreader:
        if monthCount == 0:
            previousRow = float(row[1])
        monthCount = monthCount + 1
        totalPL = totalPL + float(row[1])
        currentChange = (float(row[1]) - previousRow)
        change = change + (float(row[1]) - previousRow)
        previousRow = float(row[1])
        if currentChange > inc:
            inc = currentChange
            incDate = row[0]
        if currentChange < dec:
            dec = currentChange
            decDate = row[0]
avgChange = change / (monthCount - 1)
'{:2f}'.format(avgChange)


print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {monthCount}")
print(f"Total: ${int(totalPL)}")
print(f"Average Change: ${'{:.2f}'.format(avgChange)}")
print(f"Greatest Increase in Profits: {incDate} (${int(inc)})")
print(f"Greatest Decrease in Profits: {decDate} (${int(dec)})")

file = open("Desktop/python-challenge/PyBank/analysis/analysis.txt","w")
file.write("Financial Analysis")
file.write("\n")
file.write("-------------------------")
file.write("\n")
file.write(f"Total Months: {monthCount}")
file.write("\n")
file.write(f"Total: ${int(totalPL)}")
file.write("\n")
file.write(f"Average Change: ${'{:.2f}'.format(avgChange)}")
file.write("\n")
file.write(f"Greatest Increase in Profits: {incDate} (${int(inc)})")
file.write("\n")
file.write(f"Greatest Decrease in Profits: {decDate} (${int(dec)})")
file.close()

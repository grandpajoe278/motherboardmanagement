#!/usr/bin/python3
import csv
import sys

if len(sys.argv) > 2: #This writes to the CSV file a MOTHERBOARD_NAME, PRICE BOUGHT, PRICE SOLD and automatically computes PROFIT and puts it in too.
    sys.argv[1] = sys.argv[1].replace("_", " ")
    print(sys.argv[1:])

    with open("/Users/ichen/Documents/PythonTests/M.csv", 'a', encoding="utf-8") as f:

        Titles = ["Board", "Bought Price", "Sold Price", "~Profit"]
        writer = csv.DictWriter(f, fieldnames=Titles)

        profit = str(float(float(sys.argv[3])-(1.23*float(sys.argv[2])+15.00)))
        writer.writerow({"Board":sys.argv[1], "Bought Price":sys.argv[2], "Sold Price":sys.argv[3], "~Profit":int(float(profit)*100+0.5)/100})

    with open("/Users/ichen/Documents/PythonTests/M.csv", 'r', encoding="utf-8") as f:
        excel = csv.reader(f)
        for line in excel:
            print(line)
elif len(sys.argv) > 1 and len(sys.argv) <= 2: #This takes 1 input, and returns the price it must be sold at to break even.
    x = float(sys.argv[1])
    print(("$")+(str(int((1.23*x+15)*100+0.5)/100.0))+(" is the selling price needed to break even"))
else:  #This prints the total profit on the Terminal.
    with open("/Users/ichen/Documents/PythonTests/M.csv", 'r', encoding="utf-8") as f:
        excel = csv.reader(f)
        Total_Profit = 0.00
        for line in excel:
            Total_Profit += float(line[3])
        print(("$")+str(int(float(Total_Profit)*100+0.5)/100)+(" of approximate total profit"))




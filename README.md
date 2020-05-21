# motherboardmanagement
SETUP:
M.csv is my spreadsheet file that keeps track of all motherboard details. Before running the program, edit the code so that the file path is correct and pointing to where YOU downloaded M.csv . "M.csv" is referenced in the code 3 times. The references have this format: "with open("FILE_PATH/m.csv", "......") as f:

ABOUT & HOW TO USE:
Writes details (name, price bought, price sold) to a .csv file while also recording the profit. Also calculates necessary selling price for a given buying price. Can also return total profit.

3 different functions built in (through commandline):

1. Write details about board to .csv file. Profit will be recorded automatically based on a formula.
Input format: "python3 MotherboardManager.py BOARD_NAME PRICE_BOUGHT PRICE_SOLD", PROFIT will be calculated automatically and stored to csv file.
Example: "python3 MotherboardManager.py ASUS_P8Z77V 45.00 69.00"

2. Return the price necessary to break even when flipping a motherboard. Input is the buying price. The selling price will be returned automatically. Only put in the price of the item+shipping, do not input taxes (~6%) since that is calculated automatically. 
Example: "python3 MotherboardManager.py 29.99"

3. Calculate total profits, taken by adding up all the PROFIT cells in the file  M.csv . No input necessary.
Example: "python3 MotherboardManager.py"




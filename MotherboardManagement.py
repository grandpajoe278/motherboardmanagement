# WELCOME TO THE MOTHERBOARD MANAGEMENT CODE! THIS WILL BE UPDATED TO BE EASIER TO UNDERSTAND.
import csv
import os
import sys

listname = 'M.csv'


# Clear console screen
def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


# Remove empty lines in the file to avoid error in processing
# DO NOT RUN IF UNSURE THE FILE EXIST, FILE CHECK REQUIRED
def remove_empty():
    with open(listname, 'r') as f:
        lines = f.readlines()
    with open(listname, 'w') as f:
        lines = filter(lambda x: x.strip(), lines)
        f.writelines(lines)


class Board:
    name = ''
    brought = 0.0
    sold = 0.0
    profit = 0.0
    breakeven_point = 0.0

    def init(self):  # Input board information from console
        print('Please Enter')
        self.name = input('Motherboard Name:')
        try:
            self.brought = float(input('Brought Price   :$'))
            self.sold = float(input('Sold Price      :$'))
        except ValueError:
            print('Bruh, please input some numbers!')

    def gen_profit(self):
        self.profit = float(self.sold - (1.23 * self.brought + 15.00))
        return self.profit

    def write_to_csv(
            self):
        # This writes to the CSV file a MOTHERBOARD_NAME, PRICE BOUGHT, PRICE SOLD and automatically
        # computes PROFIT and puts it in too.
        mode = 'a' if os.path.exists(listname) else 'w'
        with open(listname, mode, encoding="utf-8") as f:
            Titles = ["Board", "Bought Price", "Sold Price", "~Profit"]
            writer = csv.DictWriter(f, fieldnames=Titles)

            writer.writerow({"Board": self.name, "Bought Price": self.brought, "Sold Price": self.sold,
                             "~Profit": int(float(self.gen_profit()) * 100 + 0.5) / 100})

        # The program above works, but write bizarre empty line to the end of the
        # file, removing them now
        # If the cause of that issue is found and fixed, this line and the function can be removed safely
        remove_empty()


# Calculate total profit from file
def calc_total():
    # Perform file check
    if os.path.exists(listname):
        # Removes empty lines in the file to avoid runtime error, can be safely removed if the bug is
        # fixed
        remove_empty()
        with open(listname, 'r', encoding="utf-8") as f:
            excel = csv.reader(f)
            Total_Profit = 0.00
            try:
                for line in excel:
                    Total_Profit += float(line[3])
                    print(("$") + str(int(float(Total_Profit) * 100 + 0.5) / 100) + " of approximate total profit")
            except ValueError:
                print('Value Error!\nA string is found at where a number is supposed to go in. \n Check your '
                      'file and make sure it is formatted correctly.')

            except Exception as e:  # Error Handling
                print('Runtime Error:', e)
                print('The program will now continue. If the error persist, contact the developer')
                print('Check your file and make sure it is formatted correctly.')
    else:
        print('File is empty. Please add a board to continue')


# Calculate breakeven by the formula
def breakeven(x):
    return int((1.23 * float(x) + 15) * 100 + 0.5) / 100.0


# Simply Print the list
def print_list():
    # Perform file check
    if os.path.exists(listname):
        # Removes empty lines in the file to avoid runtime error, can be safely removed if the bug is
        # fixed
        remove_empty()
        with open(listname, 'r', encoding="utf-8") as f:
            excel = csv.reader(f)
            try:
                for line in excel:
                    print(line)
                    # This can be more polished
            except Exception as e:  # Error Handling
                print('Runtime Error:', e)
                print('The program will now continue. If the error persist, contact the developer')


menu_message1 = '''Welcome to MotherboardManagement
    By Isaac Chen and Joe Yu
                
Current filename: '''

menu_message2 = '''
--------------------------------
[1] Add a board
[2] Calculate breakeven for a price 
[3] View full list
[4] Calculate total profit
[5] Change filename
[6] Exit'''

if __name__ == '__main__':
    if len(sys.argv) > 1:
        listname = sys.argv[1]
    while True:
        clear()
        print(menu_message1 + listname + menu_message2)
        operation = input()
        if operation == '1':
            b = Board()
            b.init()
            b.gen_profit()
            print("Profit is $" + str(b.profit))
            next_step = input('Write to file? Y/N\n')  # Prompting user to write to file
            if next_step == 'y' or next_step == 'Y':
                b.write_to_csv()
            input('Press Enter To Continue')

        elif operation == '2':  # This takes 1 input, and returns the price it must be sold at to break even.
            x = input('Brought Price		:')
            print("$" + (str(breakeven(x)) + " is the selling price needed to break even"))
            input('Press Enter To Continue')

        elif operation == '3':
            print_list()
            input('Press Enter To Continue')

        elif operation == '4':  # This prints the total profit on the Terminal.
            calc_total()
            input('Press Enter To Continue')

        elif operation == '5':
            listname = input('Please enter new filename, include suffix (.csv):')
            input('Press Enter To Continue')

        elif operation == '6':
            print('Have a good day!')
            break
        else:
            print("Wrong Operation, Please input 1-5")
            input('Press Enter To Continue')

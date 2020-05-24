# WELCOME TO THE MOTHERBOARD MANAGEMENT CODE! THIS WILL BE UPDATED TO BE EASIER TO UNDERSTAND.
import csv
import os
import sys

list_name = 'M.csv'  # The file name that the program uses


# Clear console screen
def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')


# Remove empty lines in the file to avoid error in processing
# DO NOT RUN IF UNSURE THE FILE EXIST, FILE CHECK REQUIRED, WILL THROW ERROR IF FILE DOESN'T EXIST
def remove_empty():
    with open(list_name, 'r') as f:
        lines = f.readlines()  # Read all the lines
    with open(list_name, 'w') as f:
        lines = filter(lambda x: x.strip(), lines)  # remove all blank lines by filtering
        f.writelines(lines)  # write it all back


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
        except ValueError:  # Bruh who is putting strings here, I hope it's a accident
            print('Bruh, please input some numbers!')

    def gen_profit(self):
        self.profit = float(self.sold - (1.23 * self.brought + 15.00))  # Applying formula
        return self.profit

    def write_to_csv(
            self):
        # This writes to the CSV file a MOTHERBOARD_NAME, PRICE BOUGHT, PRICE SOLD and automatically
        # computes PROFIT and puts it in too.
        mode = 'a' if os.path.exists(list_name) else 'w'
        with open(list_name, mode, encoding="utf-8", newline='') as f:
            titles = ["Board", "Bought Price", "Sold Price", "~Profit"]
            writer = csv.DictWriter(f, fieldnames=titles)

            writer.writerow({"Board": self.name, "Bought Price": self.brought, "Sold Price": self.sold,
                             "~Profit": "{0:.2f}".format(self.gen_profit())})

        # The program above works, but write bizarre empty line to the end of the
        # file, removing them now
        # If the cause of that issue is found and fixed, this line and the function can be removed safely
        # SOLVED
        # remove_empty()


# Calculate total profit from file
def calc_total():
    # Perform file check
    if os.path.exists(list_name):
        # Removes empty lines in the file to avoid runtime error, can be safely removed if the issue mentioned on
        # line 62 is fixed (maybe, leaving it here will help with blank lines unintentionally created)
        # SOLVED
        # remove_empty()
        with open(list_name, 'r', encoding="utf-8") as f:
            excel = csv.reader(f)
            total_profit = 0.00
            try:
                for line in excel:  # Going over each line
                    total_profit += float(line[3])  # Add profit from each line's fourth column
                print("$" + "{0:.2f}".format(float(total_profit)) + " of approximate total profit")
            except ValueError:  # If cannot covert to float, notify the user
                print('Value Error!\nA string is found at where a number is supposed to go in. \n Check your '
                      'file and make sure it is formatted correctly.')

            except Exception as e:  # Error Handling
                print('Runtime Error:', e)
                print('The program will now continue. If the error persist, contact the developer')
                print('Check your file and make sure it is formatted correctly.')
    else:  # The file is not there.
        print('File is empty. Please add a board to continue')


# Calculate break even by the formula
def break_even(x):
    return "{0:.2f}".format(1.23 * float(x) + 15)  # Applying formula, returns string


# Simply Print the list
def print_list():
    # Perform file check
    if os.path.exists(list_name):
        # Removes empty lines in the file to avoid runtime error, can be safely removed if the issue mentioned on
        # line 62 is fixed (maybe, leaving it here will help with blank lines unintentionally created)
        # SOLVED
        # remove_empty()
        with open(list_name, 'r', encoding="utf-8") as f:
            excel = csv.reader(f)
            try:
                for line in excel:
                    print(line)
                    # TODO This can be more polished
            except Exception as e:  # Error Handling
                print('Runtime Error:', e)
                print('The program will now continue. If the error persist, contact the developer')


# Add two parts of the welcome message, will be put together added with the list_name
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
    if len(sys.argv) > 1:  # If an argument is passed, set the list_name
        list_name = sys.argv[1]
    while True:
        clear()
        print(menu_message1 + list_name + menu_message2)  # Merge the welcome message, adding the list_name
        operation = input()
        if operation == '1':  # Process a new board
            b = Board()
            b.init()
            print("Profit is $" + str(b.gen_profit()))
            next_step = input('Write to file? Y/N\n')  # Prompting user to write to file
            if next_step == 'y' or next_step == 'Y':
                b.write_to_csv()
            input('Press Enter To Continue')

        elif operation == '2':  # This takes 1 input, and returns the price it must be sold at to break even.
            x = input('Brought Price		:')
            print("$" + (break_even(x) + " is the selling price needed to break even"))
            input('Press Enter To Continue')

        elif operation == '3':  # Simply output the list
            print_list()
            input('Press Enter To Continue')

        elif operation == '4':  # This prints the total profit on the Terminal.
            calc_total()
            input('Press Enter To Continue')

        elif operation == '5':  # Rename list_name
            list_name = input('Please enter new filename, include suffix (.csv):')
            input('Press Enter To Continue')

        elif operation == '6':  # Bye
            print('Have a good day!')
            break
        else:  # Input out of range
            print("Wrong Operation, Please input 1-6")
            input('Press Enter To Continue')

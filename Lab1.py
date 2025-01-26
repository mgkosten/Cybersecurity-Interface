"""
Cybersecurity Lab 1
Maddie Kosten
CS 2660 / Spring 2025

This program allows a user to log in to access varius pages. The program
double checks that credentials to log in are matched. It prompts the user 
to access different menu items. The access each user has is determined off
the username, password checking file access.csv.
"""
import csv
import os

# dictionary of what access letter has access to what files
ACCESS_DICT = {'A': [1, 2, 3, 4],
              'B': [1, 2, 3],
              'C': [1, 3],
              'D': [3, 4],
              'F': [0]}

# menu options/files that can possibly be accessed
MENU = {1: 'Accounting',
        2: 'Engineering Documents',
        3: 'Time Reporting',
        4: 'Reports'}

# access level for person logging in (default to no access to anything)
access_level = 'F'

def intInput(prompt, low, high):
    """ Takes the prompt, lowest possible int input, and highest possible
    int input and asks the user for an integer input based on the prompt.
    It validates that it is a number and is within the correct range.
    Returns  valid integer choice.
    """
    while 1:
        try:
            # collect users integer input choice
            choice = int(input(prompt))
            # double check int is within the correct range       
            if choice < low or choice > high:
                print('Insert an integer in the range ' + str(low) + ' to ' + str(high) + '. ')
            else:
                return choice
        # if user inputs something not an int
        except ValueError:
            print('Invalid input! Insert a integer.')

def login():
    """ Takes no paramaters. It asks the user to log in. It then 
    proceeds to make sure the username and password were valid and 
    match the access.csv file containing username, password, and access
    level. Returns true if valid login, and false otherwise.
    """
    # get path to current file
    script_dir = os.path.dirname(__file__)
    # make it path to the access.csv file
    file_path = os.path.join(script_dir, "access.csv")
    # ask user for credentials
    print('To login, enter your crdentials')
    # collect users username and password
    username = input('Username: ')
    password = input('Password: ')
    try:
        # open access.csv file
        with open(file_path, "r") as f:
            reader = csv.reader(f, delimiter=",")
            # read through each row in csv file
            for row in reader:
                # check if username and password match ones on file
                if row[0] == username and row[1] == password:
                    print('You are now logged in!')
                    # change access level to level of appropriate user
                    global access_level
                    access_level = row[2]
                    return True
        print('Something went wrong!')
        return False
    # if file could not be found 
    except FileNotFoundError:
            print(f'access.csv cannot be found!')

def menuChoices():
    """ Takes no paramaters, prints the menu options and takes the users
    choice of where they want to go. It returns the users choice value. 
    """
    print('1. Accounting\n2. Engineering Documents\n3. Time Reporting\n4. Reports')
    # collect user choice of menu options
    choice = intInput('Press the number of menu item you want to go to: ', 1, 4)
    return choice

def accessCheck():
    """ Takes no paramaters. It determines if user has valid access to
    the file they are trying to access. If not allowed to access prompts 
    user to quit or go back to the main menu and choose again. If accessed return true
    otherwise return false.
    """
    # set accessed to false automatically
    accessed = False
    # copy list of accessable files of user
    access_list = ACCESS_DICT[access_level]
    # collect users choice of menu options
    user_choice = menuChoices()
    # check if user has access to file trying to access
    for item in access_list:
        if item == user_choice:
            print('You have now accessed the ' + MENU[user_choice] + ' application')
            accessed = True
            return True
    if not accessed:
        print('You are not authorized to access ' + MENU[user_choice] + ' application')
        # not allowed to access, give option return to menu or quit
        return_choice = intInput('Press 1 to return back to the main menu; otherwise press 2 to exit. ', 1, 2)
        if return_choice == 1:
            accessCheck()
        return False


if __name__ == "__main__":
    if login():
        accessCheck()

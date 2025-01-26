# Cybersecurity-Interface

Detailed README.md (or .txt) file including a description of your program and testing instructions

## Explaining the program

This program allows a user to login to access different menu files. Each user has its own access rights. This makes it so that only certain users have access to certain files. For example one person could access all of the menu options while someone else could only access two of them. 

Logistics of program:
If user is able to successfully login, meaning they entered the correct username and password, they are shown with a menu. They then have the choice to choose one of the menu options by entering the number they want to access. If they have the access rights to the menu option, the screen will display that they have accessed that application. However, if they did not have access, it says that they are not authorized to access that document and gives them the option to exit or return back to the main menu. Exiting ends the program, and going back to the menu gives them another chance to select a menu item. Additionally, if the user does not provide the correct username and password, the program ends telling them something went wrong.

## Testing instructions
1. Attempt logging in with a valid username and password from the access.csv file (a row across). For test purposes use username: jim, password: jim
    - should pring You are now logged in and print the menu options prompting to choose one 
2. When logging in with username jim and password jim, attempt to access menu item #2.
     - This should give a failure to access that specific document error.
4. After given the choice to quit or go back to menu due to failure to access document in the previous step, try to go back to the menu (option #1)
     - Should be able to get back to the printed menu
6. After getting back to the menu from the previous step, try to access another document not allowed, so menu item #4.
     - Should show that you also do not have access to that document, and ask for you to go back to menu or exit.
8. This time try the exit option (#2).
     - This should end the program causing you to have to run it again to attempt more things.
10. Try logging in with a different set of credentials. You can do so by looking at the access.csv. The first item in a row is the username, the second is the password, and the third is the access level they have. (for example could log in with username: mk and password: mk)
      - Should be able to successfully login as in the first step.
12. This time access a document that is allowed. You can check what menu items they have access to by checking the ACCESS_DICT at the top of the python file. Whatever access level is with their login credentials is what numbered menu items they have access to. For example {'B': [1, 2, 3]} has access to menu options #1, #2, and #3. (If used mk, they have access menu items 1-3)
     - This should cause the prompt you have accessed that specific file, and end the program.
13. Next, attempt logging in with invalid credentials. These are credentials that do not match any in the csv file. (could try username: uvm and password: catamount)
     - This should say something went wrong and end the program. 
14. Now try deleting the access.csv file or moving it to another folder such that it is not in the same file as the python file.
15. Now try running the program again. Login with any credential (can test one time with one that is on the access.csv file and then test another time (when run program again) with one that is not on the file)
     - Any credential should fail due to the program not being able to reach access.csv. It should print that access.csv cannot be found. 

# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created starter script (future script!)
# Kenji Petrucci, 8/9/2022; Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
file = "ToDoList.txt"   # An object that represents a file
data = ""  # A row of text data from the file
rows = {}    # A row of data separated into elements of a dictionary {Task,Priority}
table = []  # A list that acts as a 'table' of rows
menu = ""   # A menu of user options
sel = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
obj = open(file, "a")  #create file if it doesn't exist, append
obj.close()

obj = open(file, "r")  #read existing file data
for row in obj:
    lstrow = row.split(",")
    rows = {"task":lstrow[0], "priority":lstrow[1].strip()}  #define keys and values
    table.append(rows)
obj.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Please Select From the Following Menu Options:
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    sel = input("Enter Selection [1 to 5]: ")
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (sel.strip() == '1'):
        print("Existing data: ")
        for row in table:
            print(row)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (sel.strip() == '2'):
        task = input("Enter Task Name: ")
        priority = input("Enter Priority: ")
        rows = {"task":task, "priority":priority}  #add values (user input) to defined keys
        table.append(rows)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (sel.strip() == '3'):
        i = 0  #define increment counter to define row nummers for deletion
        print("Existing data: ")
        for row in table:
            i = i + 1
            print(str(i) + str(row))  #displays row numbers
        delete = int(input("Select row number for deletion: ")) -1  #subtract 1 from user input since i starts at 0
        del table[delete]  #delete selected row
        for row in table:
            print(row)  #verify deletion
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (sel.strip() == '4'):
        obj = open(file, "a")
        for row in table:
            obj.write(str(row) + "\n")
        obj.close()
        print("saved to file")
        continue
    # Step 7 - Exit program
    elif (sel.strip() == '5'):
        break  # and Exit the program

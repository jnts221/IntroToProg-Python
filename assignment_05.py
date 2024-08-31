# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Sohail Nassiri,08/31/2024,Created Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "enrollments.csv"  # Set the csv file name

# Define the Data Variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str = ''  # Hold the choice made by the user.

# When the program starts, read the file data into a list of dictionary rows (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")  # Reads file
    for row in file.readlines():  # Reads through each line
        # Transform the data from the file
        student_data = row.split(",")  # Splits string into a list of dictionary rows using a comma separator
        student_data = {"FirstName": student_data[0],
                        "LastName": student_data[1],
                        "CourseName": student_data[2].strip()}  # Removes unnecessary spaces and carriage returns
        # Load it into our collection (list of dictionary rows)
        students.append(student_data)  # Adds data to two-dimensional table
    file.close()
except FileNotFoundError as e:  # Raises exception if file is not found
    print("Text file must exist before running this script!\n")  # Prints custom message
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep="\n")  # Provides details of error
except Exception as e:  # Raises any other general exception that is not specifically called out
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep="\n")
finally:
    if file:
        file.close()  # Closes file regardless of whether code successfully executes or not

# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():  # Requires user to input alphabetical name
                raise ValueError("The first name should not contain numbers.")  # Raises error if non-alphabetical
            # character is entered
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)  # Table is appended with data from list of dictionary row
            print(
                f"You have registered {student_first_name} {student_last_name} for {course_name}.")  # Displays inputted
            # registration
        except ValueError as e:
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep="\n")
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep="\n")
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-" * 50)
        for student in students:  # Iterates through each row of table
            print(
                f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")
        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")  # Opens file in write mode
            for student in students:
                csv_data = f"{student["FirstName"]},{student["LastName"]},{student["CourseName"]}\n"
                file.write(csv_data)  # Writes the content of the csv_data variable to the file
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(
                    f"Student {student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")
        except FileNotFoundError as e:
            print("Text file must exist before running this script!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep="\n")
        except Exception as e:
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep="\n")
        finally:
            if file:
                file.close()
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")  # Returns user to menu if invalid selection made

print("Program Ended")

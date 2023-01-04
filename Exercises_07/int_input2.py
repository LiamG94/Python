"""

Script: int_input2.py
By: Liam Gallagher
Purpose: Raise an exception to make sure a value greater than 0 is entered
Tested on: Python 3.10.7 using Windows 10

"""

# Take an input number as a string and convert it to an integer
my_value = int(input("Enter an integer greater than 0"))
if my_value <= 0:
 raise Exception("Values must be > 0 ")
else:
 print("Validation checks passed")
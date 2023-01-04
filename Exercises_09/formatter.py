"""

Script: formatter.py
By: Liam Gallagher
Purpose: Shows different ways of formatting a string
Tested on: Python 3.10.7 using Windows 10

"""

#Method to convert a string to upper case
def convert_upper(my_text):
 return my_text.upper()
#Method to convert a string to lower case
def convert_lower(my_text):
 return my_text.lower()
#Method to convert the first character in a string to a capital, 
#and the rest of the string to lower case
def convert_capital(my_text):
 return my_text.capitalize()
 
print(convert_lower("John ORaw"))
print(convert_upper("John ORaw"))
print(convert_capital("dUBLIN"))

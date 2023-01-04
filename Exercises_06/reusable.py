'''

Script: reusable.py
By: Liam Gallagher
Purpose: To create code that can be used by other modules
Tested on: Python 3.10.7 using Windows 10

'''
#Create a function to be used by other modules
def my_square(a: int)->int:
 print("Running code from the module")
 return a*a

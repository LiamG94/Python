'''

Script: cube.py
By: Liam Gallagher
Purpose: A module with a function that cubes a number
Tested on: Python 3.10.7 using Windows 10

'''

cube_text = "Yo, time to cube stuff!"
#Function that cubes a number but also lets us know where the function is being called from
def cube(x):
 return x*x*x
#If the function is being called by this script
if (__name__ == '__main__'):
 print(f"This module is called {__name__} and executes as a standalone script")
#If the function is being called by a different script
else:
 print(f"This module is called {__name__} and is being called by another script")

'''

Script: my_if.py
By: Liam Gallagher
Purpose: To show the functionality of If, Elif and Else Statements
Tested on: Python 3.10.7 using Windows 10

'''

a = False
b = False
c = False

if a:
 #Display if 'a' is True
 print("a was true")
elif b:
 #Display if 'b' is True
 print("b was true")
elif c:
 #Display if 'c' is True
 print("c was true")
else:
 #Display if none of them return True
 print("None of our boolean variables were true")


if (3<2) and (5<9):
 #Display if both are True
 print("Yup!")
elif (3<2) or (5<9):
 #Display if one of the answers is True
 print("Nearly!")
else:
 #Display if none are True
 print("Nope!")
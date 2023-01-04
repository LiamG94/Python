'''

Script: library2.py
By: Liam Gallagher
Purpose: To show how a specific function can be imported
Tested on: Python 3.10.7 using Windows 10

'''
#Imports just the sqrt function from the math package
from math import sqrt
print("Input lengths of the two short triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
#No longer need to call the package to access the function
c = sqrt(a**2 + b**2)
print("The length of the hypotenuse to four decimal places is: {hypo:1.4f}".format(hypo=c))

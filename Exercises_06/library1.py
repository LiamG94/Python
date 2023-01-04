'''

Script: library1.py
By: Liam Gallagher
Purpose: To show the use of the 'math' library
Tested on: Python 3.10.7 using Windows 10

'''
import math
print("Input lengths of the two short triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
#Call the sqrt function from the math package
c = math.sqrt(a**2 + b**2)
print("The length of the hypotenuse to four decimal places is: {hypo:1.4f}".format(hypo=c))
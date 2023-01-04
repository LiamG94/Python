'''

Script: project2.py
By: Liam Gallagher
Purpose: To access the functions from both square.py and cube.py
Tested on: Python 3.10.7 using Windows 10

'''
#Import the two modules
import mylib.cube as mycube
import mylib.square as mysquare
#Call the functions from within each module
print(mycube.cube_text, mycube.cube(3))
print(mysquare.square_text, mysquare.square(3))
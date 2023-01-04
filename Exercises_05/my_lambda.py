'''

Script: my_lambda.py
By: Liam Gallagher
Purpose: To show the functionality of the lambda() function 
Tested on: Python 3.10.7 using Windows 10

'''

#Calculate the circumference using a lambda function
circumference = lambda radius : 2 * 3.142 * radius
#Calculate the area using a lambda function
area = lambda radius : 3.142 * radius * radius
#Set a value for the radius
radius = 5
#Display the results by calling both functions
print(circumference(radius), area(radius))

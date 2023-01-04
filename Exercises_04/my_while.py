'''

Script: my_while.py
By: Liam Gallagher
Purpose: To show the functionality of While Loops
Tested on: Python 3.10.7 using Windows 10

'''

x = 0
while x < 10:
 #while 'x' is less than 10, display 'x' then add 1 to it
 print(f"X is = {x}")
 x = x + 1
#Loop finishes when the 'while condition' is no longer true
#Execute the 'else' statement if there is one after this
else:
 print(f"As x is now = {x}, we are all finished")
 
my_list = []
my_string = "Morning Folks!"
#For each letter in the string, add it as an individual entry to the list
for letter in my_string:
 my_list.append(letter)
print(my_list)

my_string = "Morning Folks!"
#For each letter in the string, add it as an individual entry to the list
my_list = [letter for letter in my_string]
print(my_list)

#Add each number in the range 0 to 20 to the list
my_list = [number for number in range(0,20)]
print(my_list)

#Multiply each number in the range 0 to 20 by 10 and add it to the list
my_list = [number * 10 for number in range(0,20)]
print(my_list)

#Multiply each number in the range 0 to 20 by 10,
#but only add it to the list if the number is less than 10
my_list = [number * 10 for number in range(0,20) if number < 10]
print(my_list)

conversion = 0.3048
#List in feet
my_depth_in_feet = [12.3, 13.8, 15.3, 12.1, 8.8]
#Populate a new list with each entry from 'my_depth_in_feet' converted to meters
my_depth_in_meters = [(depth * conversion) for depth in my_depth_in_feet]
print(my_depth_in_meters)
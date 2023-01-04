'''

Script: my_map.py
By: Liam Gallagher
Purpose: To show the functionality of the map() function
Tested on: Python 3.10.7 using Windows 10

'''

def double_number(n: int)->int:
 """
 Simple function to double a number
 """
 return n+n
# Create a list of numbers for testing
my_numbers = [1,2,3,4,5]
# Map my_numbers to the double_number function, return type is map
result = map(double_number, my_numbers)
# Print a list of the map
print(list(result))
# Or iterate through it
for item in map(double_number, my_numbers):
 print(item)

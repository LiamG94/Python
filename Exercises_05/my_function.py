'''

Script: my_function.py
By: Liam Gallagher
Purpose: To show the functionality of Functions
Tested on: Python 3.10.7 using Windows 10

'''

def test_function():
 #Simple test function
 print("Yoo hoo!")
 
test_function()

def test_function2(first_name):
 #Simple test function
 print(f"Yoo hoo, hello {first_name}!")
 
test_function2("Liam")

def calculate_circumference(radius):
 #Calculate the circumference of a circle based on its radius
 return 2 * 3.142 * radius
 
a = calculate_circumference(5)
print(f"The circumference is: {a}")

#Use a default value to avoid a runtime error
def calculate_circumference(radius = 1):
 #Calculate the circumference of a circle based on its radius
 return 2 * 3.142 * radius
 
a = calculate_circumference()
print(f"The circumference is: {a}")

def calculate_circumference2(radius):
 #Calculate the circumference of a circle based on its radius
 return 2 * 3.142 * radius
 
#Get a radius value as a string
r = input("Provide a radius value: ")
#Convert it to a float
r_float = float(r)
#Call the function and create the variable for the return value
a = calculate_circumference2(r_float)
print(f"The circumference is: {a}")

#Use a '*' to pass an unknown number of arguments to the function
def auto_adder(*my_numbers):
 final_number = 0
 #Loop to add all the numbers together
 for number in my_numbers:
  final_number = final_number + number
 return final_number
#Call the function and pass in variables
total = auto_adder(12,34,23,66,8, 99)
print(f"The total is: {total}")



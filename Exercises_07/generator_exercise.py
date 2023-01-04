"""

Script: generator_exercise.py
By: Liam Gallagher
Purpose: Exercise to highlight the importance of exception handling
Tested on: Python 3.10.7 using Windows 10

"""

"""
Function to calculate how long the generator will run for
Returns a float representing the minutes of use left
"""
def calculate_endurance(fuel: float, fuel_consumption: float)->float:
  #Exception handling for the calculation, try to divide
  try:
   endurance = fuel/fuel_consumption
  #If trying to divide by 0, return 0
  except ZeroDivisionError:
    return 0
  #Otherwise, return the result
  else:
   return round(endurance)

"""
Function that asks the user to add fuel to the generator
It then asks whether the generator is in use
Depending on the users response, the function will print a particular statement
"""
def remaining_endurance():
 #Endless loop until the desired result is entered
 while True:
  #Exception handling for the user input, try to get a number as a response
  try:
   fuel = float(input("Enter fuel in litres to the generator: "))
  #A number wasn't entered
  except:
   print("Enter an number only!")
  #If a number was entered
  else:
   #Check to make sure it is a positive number
   if fuel <= 0:
     print("You must add some fuel")
   #Otherwise break from the loop
   else:
    break
    
 #Create fuel consumption variable showing fuel consumed per minute 
 fuel_consumption = 0.14
 
 #Endless loop until the desired result is entered
 while True:
  #Exception handling to make sure that only 'Y' or 'N' has been entered
  try:
   idling_input = str(input("Is the motor in use (Y/N): "))
  #A string was not entered
  except:
   print("Enter 'Y' or 'N' only!")
  #A string was entered
  else:
   #Make the string lower case
   idling_input = idling_input.lower()
   #The motor is in use
   if idling_input == "y":
    #Print the result by calling the calculate_endurance function
    print(f"Minutes until the tank is empty: {calculate_endurance(fuel, fuel_consumption)}")
    break
   #The motor is idling
   elif idling_input == "n":
    print("The motor is idling, no fuel is being consumed")
    break
   #A string was not entered
   else:
    print("Enter 'Y' or 'N' only!")
       

#Call the function to run the code
remaining_endurance()

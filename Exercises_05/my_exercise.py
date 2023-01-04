'''

Script: my_exercise.py
By: Liam Gallagher
Purpose: To demonstrate what has been shown in Walkthrough 6
Tested on: Python 3.10.7 using Windows 10

'''

"""
Function to see if the remainder after dividing the two numbers equals 0
Returns a True or False answer
"""
def divisible(numerator: int, denominator: int)->bool:
 #Returns True if the numerator modulus the denominator equals 0, otherwise it will return False
 return numerator % denominator == 0
print(divisible(30,4))
"""
If the variables passed into the function are changed so that the remainder equals 0,
the function will return True
"""
#print(divisible(32,4))


"""
Function to see if a number matches any of the numbers in a list
Will return True if the number is in the list,
but will not return False as we did not specify this in our else statement
This results in 'None' being returned
"""
def find_num(number_list: list, number: int)->bool:
 #For each number in the list
 for iterate_number in number_list:
  #If this iteration matches the number we are looking for, return True
  if iterate_number == number:
   return True
  else:
   #pass
   """
   Instead of above 'else' statement using the pass function to move onto the next iteration,
   I would first use the below code to return False if the number is not found
   """
   #Return False if we have reached the end of the list
   #I take one away from the length of the list as the index of the list begins at 0
   if number_list.index(iterate_number) == len(number_list)-1:
    return False
    #break from the loop
    break
   #Otherwise move to the next iteration
   else:
    pass

result = find_num([1,2,3,4,5,6,7,8],9)
if result == True:
 print("The number is in the list!")
else:
 print("The number wasn't found.")

"""
If we changed one of the numbers in the list to '9' then the function would return True
We could also change the number we are looking for to something that matches a number in the list
"""

"""
Function to find out if there is an even number in a list
"""
def find_num(number_list: list)->bool:
 #For each number in the list
 for iterate_number in number_list:
  #If this iteration matches the number we are looking for, return True
  if iterate_number % 2 == 0:
   return True
   #break from the loop
   break
  else:
   #Return False if we have reached the end of the list
   #I take one away from the length of the list as the index begins at 0
   if number_list.index(iterate_number) == len(number_list)-1:
    return False
    #break from the loop
    break
   #Otherwise move to the next iteration
   else:
    pass
result = find_num([1,2,3,4,5,6,7,8])

if result == True:
 print("There is an even number in the list!")
else:
 print("The list only contains odd numbers.")



#Calculate the volume of a cylinder using a lambda function
volume = lambda height, radius: 3.142 * (radius*radius) * height
#Set a value for the height and radius
radius = 5
height = 20
#Display the results by calling both functions
print("The volume is:",volume(height, radius))
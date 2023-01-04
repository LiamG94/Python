'''

Script: my_if.py
By: Liam Gallagher
Purpose: To show the functionality of For Loops
Tested on: Python 3.10.7 using Windows 10

'''

iterable_variable = [1,2,3,4,5,6]
for item in iterable_variable:
 #For each item, execute this code block
 print(item)

print(end='\n')

for item in iterable_variable:
 #For each item, execute this code block
 if item %2 != 0:
  #Display if the requirements are met
  print(item)
  
print(end='\n')  
  
for item in iterable_variable:
 #For each item, execute this code block
 if item %2 == 0:
  #Display if the requirements are met
  print(item)

print(end='\n') 

total = 0
for item in iterable_variable:
 #For each item, execute this code block
 total = total + item
#print() function is not indented as we do not want it to run as part of the loop
#Instead, print the total when the loop is complete
print(total)

print(end='\n') 

#Define a string to iterate over
for this_letter in "Liam Gallagher":
 #Specify which letter to test for
 if this_letter == "G":
  #Found the test letter
  print(f"Woo hoo, found a {this_letter}!")
  #Exit the current loop
  break
 else:
  #Didn't find the test letter
  print(f"Aww man, I didn't want {this_letter}!")

print(end='\n')

my_list = [1,2,3,0]
for my_number in my_list:
 #If the number equals '1', pass to the next if statement
 if my_number == 1:
  pass
 #If the number equals '2', move to the next itteration in the loop
 if my_number == 2:
  continue
 #If the number equals '3', display the message then continue with the loop
 if my_number == 3:
  print(f"Found the number {my_number}")
 #If the number equals'0', break from the loop completely
 if my_number == 0:
  break

print(end='\n')

list_of_tuples = [(1,2), (3,4), ("A", "B")]
for item in list_of_tuples:
 print(item) 
 
print(end='\n')

#Tuple unpacking
list_of_tuples = [(1,2), (3,4), ("A", "B")]
for a,b in list_of_tuples:
 print(a)
 print(b)
 
print(end='\n')

for index in range(1, 100, 5):
 #Display every 5th index in the range 1 to 100
 print(index)


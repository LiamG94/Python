'''

Script: lists.py
By: Liam Gallagher
Purpose: To show the functionality of Lists
Tested on: Python 3.10.7 using Windows 10

'''

#Create a list
my_list1 = [1,2,3,4,"A"]
#Display the full list
print(my_list1, end='\n\n')
#Display the number of elements in the list
print(len(my_list1), end='\n\n')
#Display elements from the list starting at position '1', 
#and ending at position '3' in the list
print(my_list1[1:3:1], end='\n\n')
#Display the last entry in the list
print(my_list1[-1], end='\n\n')

#Create a second list
my_list2 = ["S","T","Fish",9,10]
#Display the two lists added together
print(my_list1 + my_list2, end='\n\n')

#Create a new list to hold both previous lists
nested_list = [my_list1,my_list2]
#Display the new list
print(nested_list, end='\n\n')

#Change the entry in position '2' of the list
my_list1[2] = "Chips"
#Display the list to highlight the change
print(my_list1, end='\n\n')

#Add en entry to the end of the list
my_list1.append(1)
#Display the change
print(my_list1, end='\n\n')
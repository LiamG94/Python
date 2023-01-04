'''

Script: lists_exercise.py
By: Liam Gallagher
Purpose: To test the different methods applicable to Lists
Tested on: Python 3.10.7 using Windows 10

'''

#Similar to .append() but instead of one entry,
#a full list can be added to the end of another list
my_list3 = [2,4,8]
my_list4 = [3,6,12]
my_list3.extend(my_list4)
print(my_list3, end='\n\n')

#Insert an entry to the list at a certain position
my_entry = 1
my_list3.insert(1, my_entry)
print(my_list3, end='\n\n')

#Remove the first entry that is equal to value entered
x = 6
my_list4.remove(x)
print(my_list4, end='\n\n')

#Removes the entry at the end of the list and returns it
print(my_list3.pop(), end='\n\n')
#Removes the entry at a given point in the list and returns it
print(my_list3.pop(2))
print(my_list3, end='\n\n')

#Removes all entries from the list
my_list4.clear()
print(my_list4, end='\n\n')

#Returns the position in the list of the first entry that equals the value entered
print(my_list3.index(8), end='\n\n')

#Counts how many times the entered value appears in the list
my_list5 = ["Bread",2,6,"Bread",6,8,6]
print(my_list5.count(6))
print(my_list5.count("Bread"), end='\n\n')

#Sorts a list either numerically or alphabetically
my_list6 = ["Liam","John","Ben"]
my_list6.sort()
print(my_list6, end='\n\n')
#Sorts the list but in reverse
my_list7 = [6,4,8,3,5]
my_list7.sort(reverse = True)
print(my_list7, end='\n\n')

#Reverses the order of the list without sorting
my_list8 = [6,4,8,3,5]
my_list8.reverse()
print(my_list8, end='\n\n')

#Makes a copy of the original list but does not modify it
my_list9 = my_list8.copy()
print(my_list9, end='\n\n')
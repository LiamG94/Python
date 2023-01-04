'''

Script: dictionaries.py
By: Liam Gallagher
Purpose: To show the functionality of Sets
Tested on: Python 3.10.7 using Windows 10

'''

#Create the Set
my_set = set()
#Display it's Type
print(type(my_set))
#Display the Set
print(my_set)
#Add some entries to the Set
my_set.add(1)
my_set.add(2)
#Try to add '2' for a second time
my_set.add(2)
print(my_set)
#Sets are a collection of unique objects so '2' cannot be added twice
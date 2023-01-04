'''

Script: tuples.py
By: Liam Gallagher
Purpose: To show the functionality of Tuples
Tested on: Python 3.10.7 using Windows 10

'''

#Square brackets for creating a list
my_list = ["one","two","three"]
#Regular brackets for creating a tuple 
my_tuple = ("one","two","three", "one")
print(type(my_list))
print(type(my_tuple), end='\n\n')

#How many times 'one' appears in the tuple
print(my_tuple.count("one"))
#The first position in the tuple we can find 'one'
print(my_tuple.index("one"), end='\n\n')

#Runtime error when trying to change a value within a tuple due to them being immutable
#my_tuple.index("one") = "two"

#There is one possible workaround if you first convert the tuple to a list,
#make your edit, then convert it back to a tuple again
tuple_conversion = list(my_tuple)
tuple_conversion[tuple_conversion.index("one")] = "two"
my_tuple = tuple(tuple_conversion)
print(my_tuple)
#To confirm the type is 'tuple'
print(type(my_tuple))
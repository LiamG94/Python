'''

Script: dictionaries.py
By: Liam Gallagher
Purpose: To show the functionality of Dictionaries
Tested on: Python 3.10.7 using Windows 10

'''

#Create the initial directory
my_dictionary = {"FName":"Liam","SName":"Gallagher","Occupation":"Duty Manager"}
#Display the full dictionary
print(my_dictionary)
#Display just the 'Occupation' within the dictionary
print(my_dictionary["Occupation"])
#Add a key:value to the dictionary
my_dictionary["Salary"] = "Not enough!"
print(my_dictionary)
#Edit a value in the dictionary
my_dictionary["Occupation"] = "Assistant Manager"
my_dictionary["Salary"] = "Slightly better"
print(my_dictionary, end='\n\n')

#Displays the 'keys' of the dictionary
print(my_dictionary.keys())

#Displays the 'values' of the dictionary
print(my_dictionary.values())

#Displays the 'items' of the dictionary
print(my_dictionary.items())
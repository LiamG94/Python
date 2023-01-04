'''

Script: kelvin_exercise.py
By: Liam Gallagher
Purpose: To convert 10 temperature readings from Kelvin to both Celsius and Fahrenheit
Tested on: Python 3.10.7 using Windows 10

'''

#10 Kelvin readings
my_kelvin_list = [273.15, 373.15, 294.15, 334.65, 302.15, 331.25, 298, 300, 317.29, 280.15]
#For each temperature reading in 'my_kelvin_list', convert it to Celsius then add it to the list
my_celsius_list = [(temp_reading - 273.15) for temp_reading in my_kelvin_list]
#For each temperature reading in 'my_kelvin_list', convert it to Fahrenheit then add it to the list
my_fahren_list = [((temp_reading - 273.15)*1.8 + 32) for temp_reading in my_kelvin_list]

for temp in my_celsius_list:
 #For each temperature, Display the change
 print(f"Celsius reading: {temp}")

print(end='\n')

for temp in my_fahren_list:
 #For each temperature, Display the change
 print(f"Fahrenheit reading: {temp}")
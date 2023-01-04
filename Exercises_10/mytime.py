"""

Script: mytime.py
By: Liam Gallagher
Purpose: To show how to get different values of time using 'datetime'
Tested on: Python 3.10.7 using Windows 10

"""

from datetime import datetime as dt
# Get the current time, returns a value like 2022-10-09 17:46:45.151666
today = dt.now()
print(today)
# Get Unix time, returns a value like 1665566809.057217
unix_epoch_time = dt.timestamp(today)
print(unix_epoch_time)

#Breaks down the 'now()' time into readable strings for each individual value
weekday = dt.now().strftime("%A")
day = dt.now().strftime("%d")
month = dt.now().strftime("%B")
year = dt.now().strftime("%Y")
hour = dt.now().strftime("%H")
minute = dt.now().strftime("%M")
second = dt.now().strftime("%S")

#Display a readable date
print(f"Today is {weekday} {day} {month} {year}")
#Diaplay a readable time
print(f"The current time is {hour}:{minute}:{second}")

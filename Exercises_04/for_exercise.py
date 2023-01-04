'''

Script: for_exercise.py
By: Liam Gallagher
Purpose: To test iteration through a dictionary 
Tested on: Python 3.10.7 using Windows 10

'''

scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}

for item in scan:
 #Display each item in 'scan'
 print(item)

for item in scan.items():
 #Display each item in 'scan'
 print(item)
 
scan = {"192.168.3.10": "80", "192.168.3.11": "443", "192.168.3.55": "22"}
for ipv4, port in scan.items():
 print(f"Found a service on {ipv4} at {port}")
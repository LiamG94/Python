"""

Script: main.py
By: Liam Gallagher
Purpose: Main script from which the different devices from 'my_device' are tested
Tested on: Python 3.10.7 using Windows 10

"""

from my_device import Firewall, Switch, LoadBalancer
# Create a firewall instance
firewall27 = Firewall("firewall27")
# Configure it
firewall27.configure_firewall()
# Create a firewall instance
firewall28 = Firewall("firewall28")
# Verify a CRC
firewall28.calculate_crc("dummy data")

# Create a switch instance
switch27 = Switch("switch27")
# Configure it
switch27.configure_switch()
# Create a switch instance
switch28 = Switch("switch28")
# Verify a CRC
switch28.calculate_crc("dummy data")

# Create a load balancer instance
loadbalancer27 = LoadBalancer("loadbalancer27")
# Configure it
loadbalancer27.configure_load_balancer()
# Create a load balancer instance
loadbalancer28 = LoadBalancer("loadbalancer28")
# Verify a CRC
loadbalancer28.calculate_crc("dummy data")

'''

Script: tuple_unpacking.py
By: Liam Gallagher
Purpose: Create a function to identify the most expensive item
Tested on: Python 3.10.7 using Windows 10

'''

def most_expensive(price_list):
 """
 Iterate through a list and find the most expensive item
 """
 # Set up the variables
 max_price = 0
 max_price_item = ""
 # Iterate, unpacking the tuple
 for description, price in price_list:
  # If this is the maximum price, record that in our variables
  if price > max_price:
   max_price = price
   max_price_item = description
  # If it is not the maximum price, do nothing
  else:
   pass
 # Return the maximum prices item and its price
 return max_price_item, max_price
# Provide the data
price_list = [("Pineapple €", 1.0), ("Apples €", 0.5), ("Pears €", 0.7), ("Peaches €", 0.8)]
# Call the function and unpack its return values
product, price = most_expensive(price_list)
#Gives an error because our function only returns two variables and not three
#product, price, availability = most_expensive(price_list)
print(product, price)


"""
Simple Class by JOR, by convention, use camel case to name classes
"""
# Create a class
class MyClass1():

 # Constructor, called whenever an instance of the class is created.
 def __init__(self, my_greeting):
  print("Running constructor for MyClass1")
  # Create attributes and set initial values
  self.message = my_greeting
  
 def my_method(self):
  print(self.message)
  
my_class1 = MyClass1("Morning John!")
my_class1.my_method()
print(type(my_class1))

class MyClass2():
 # Constructor, called whenever an instance of the class is created.
 def __init__(self, my_greeting):
  print("Running constructor for MyClass2")
  # Create attributes and set initial values
  self.message = my_greeting
  
 def my_method(self):
  print(self.message)
  
my_class2 = MyClass2("Morning Liam!")
my_class2.my_method()
print(type(my_class2))
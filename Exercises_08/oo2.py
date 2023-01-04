"""
Class template by JOR
Revision History
06OCT22: Alpha
"""

class MyTemplate():
 # Define a class object attribute, it will be the same for any instance of the class
 class_object_attribute1 = 6378137
 class_object_attribute2 = 6356752
 # Constructor, called whenever an instance of the class is created.
 def __init__(self, attribute1: str, attribute2: bool) -> None:
  print("Constructor ran")
  # Take in an argument and assign it to a meaningful attribute name
  self.attr1 = attribute1
  self.attr2 = attribute2
  
 def my_method1(self):
  if self.attr2:
   print(f"Good morning {self.attr1}")
  else:
   print(f"No greeting {self.attr1}")
   
 def my_method2(self, my_name:str):
  if self.attr2:
   print(f"Good morning {my_name}")
  else:
   print(f"No greeting {my_name}")


# Instantiate the class
my_object = MyTemplate("John", True)
# Check the object
print(my_object.class_object_attribute1, my_object.class_object_attribute2)

my_object.my_method1()
my_object.my_method2("Giovanni")



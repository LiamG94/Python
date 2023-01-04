"""

Script: test_formatter.py
By: Liam Gallagher
Purpose: To test if the string has been formatted correctly
Tested on: Python 3.10.7 using Windows 10

"""

import unittest
import formatter

class TestFormatter(unittest.TestCase):
 def test_lower(self):
  test_text = "JOHN ORAW"
  #Call method from 'formatter' to convert to lower case
  result = formatter.convert_lower(test_text)
  #Check to see if the two are the same
  self.assertEqual(result, "john oraw")
  
 def test_upper(self):
  test_text = "John ORaw"
  #Call method from 'formatter' to convert to upper case
  result = formatter.convert_upper(test_text)
  #Check to see if the two are the same
  self.assertEqual(result, "JoHN ORAW")
  
if __name__ =="__main":
 unittest.main()
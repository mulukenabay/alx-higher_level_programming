#!/usr/bin/python3
import string
 
# initialize z
z = 20
 
# printing z
print(& quot
       Number of elements required : & quot
       + str(z))
 
# Print Alphabets till z
# Using string.ascii_lowercase + slicing
res = string.ascii_lowercase[:z]
 
# printing result
print(& quot
       Alphabets till z are : & quot
       + str(res))

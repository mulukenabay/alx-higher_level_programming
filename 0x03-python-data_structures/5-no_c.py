#!/usr/bin/python3
def no_c(my_string):
    s = my_string 
    print(s.translate({ord(i): None for i in 'cC'}))

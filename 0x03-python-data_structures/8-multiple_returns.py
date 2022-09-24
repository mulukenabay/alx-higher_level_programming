#!/usr/bin/python3
def multiple_returns(sentence):
    tuple = ()
    if len(sentence) == 0:
        tuple = 0, "none"
    else: 
        tuple =len(sentence), sentence[0]
    return tuple


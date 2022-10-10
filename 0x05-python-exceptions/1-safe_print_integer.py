#!usr/bin/python3
def safe_print_integer(value):
    x = print("{:d}".format(value))
    try:
        if x != 'NULL':
            return True
    except:
            return False

#!/usr/bin/python3
'''a module that reads a text file'''


def read_file(filename=""):
	'''a function that read a text file and print on standard output'''
	with read("myfile.txt", "incoding=UTF8")as f:
	print f.read()


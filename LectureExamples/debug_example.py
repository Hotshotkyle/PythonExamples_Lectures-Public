#!/usr/bin/python3

################################
# File Name:	debugExample.py
# Author:		Chadd Williams
# Date:			10/20/2014
# Class:		CS 360
# Assignment:	Lecture Examples
# Purpose:		Demonstrate pdb, the debugger
################################




def sumTo(intValue: int) -> int :
	""" sum the numbers 0 to intValue - 1, return the result
	"""
	total = 0
	# where will show you the stack trace
	for number in range(intValue):
		# break debug_example.py:22 to set a breakpoint on the following line
		total += number
	
	return total








# break debug_example.py:34 to set a break point on the following line
intValue = 4

# continue will run to the next breakpoint

# step or next will execute one line

# print intValue will print the value in intValue
# intValue = 2 will change the value of intValue!
name = "CS 360"
# print name[1] will print the character in slot 1
print(sumTo(intValue))

intValue = sumTo(5)

print(intValue)


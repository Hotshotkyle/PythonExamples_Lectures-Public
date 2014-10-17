#!/usr/bin/python3

################################
# File Name:	LoopExamples.py
# Author:		Chadd Williams
# Date:			10/17/2014
# Class:		CS 360
# Assignment:	Lecture Examples
# Purpose:		Demonstrate Loops, sets, lists
################################




def loopOnList():
	""" loop on a list
	
	"""
	
	# note that repeats are allowed!
	names = ["Doug", "Shereen", "Chadd", "Mike", "Chris", 
		"Nancy", "Chris", "Ian", "Bill" ]
		
		
	for name in names:
		print(name)
		
	print("----------------")	
	
	for name in sorted(names):
		print(name)
		
	print("----------------")	
		

def loopOnSet():
	"""
	"""
	# Somebody needs to write this!
	
	# pass is like no op, or just typing a single ; on a
	# blank line in C/C++.
	
	pass
	

def loopOnDict():
	"""loop on a dictionary
	"""
	
	
def main():
	""" invoke each function
	
	"""
	
	loopOnList()
	loopOnSet()
	loopOnDict()
	

# invoke main()
if __name__ == "__main__":
	main()




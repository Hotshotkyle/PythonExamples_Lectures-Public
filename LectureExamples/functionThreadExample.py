#!/usr/bin/python3

################################
# File Name:	functionThreadExample.py
# Author:		Chadd Williams
# Date:			10/20/2014
# Class:		CS 360
# Assignment:	Lecture Examples
# Purpose:		Demonstrate threads via functions
################################

import time
import threading
import random

# http://www.tutorialspoint.com/python/python_multithreading.htm

# http://en.wikibooks.org/wiki/Python_Programming/Threading

			
def threadFunction () :
	""" This function will print a message to the screen then pause
	"""
	for i in range(10):
		print('\t',threading.get_ident(), (threading.get_ident()%10)*'\t', i)
		time.sleep(random.uniform(.1,.6))
		
def namedThreadFunction (name) :
	""" This function will print a message to the screen then pause
	
	This function takes one parameter, a string that is part of 
	the message printed to the screen
	"""

	for i in range(10):
		print(name, i)
		time.sleep(random.uniform(.1,.6))
		
	
# launch three threadFunction threads
threading.Thread(target=threadFunction).start()
threading.Thread(target=threadFunction).start()
threading.Thread(target=threadFunction).start()



# launch three namedThreadFunction threads

# args must be a tuple! So you MUST have a comma in the
# tuple, even if you only send one argument

threading.Thread(target=namedThreadFunction, args=("doug",)).start()
threading.Thread(target=namedThreadFunction, args=("shereen",)).start()
threading.Thread(target=namedThreadFunction, args=("chadd",)).start()



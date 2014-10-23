#!/usr/bin/python3

################################
# File Name:	TKExample.py
# Author:		Chadd Williams
# Date:			10/17/2014
# Class:		CS 360
# Assignment:	Lecture Examples
# Purpose:		Demonstrate TK
################################

from tkinter import *
from tkinter.ttk import *


class ButtonHandler:
	""" simple class that will provide methods to handle button clicks
	"""
	
	def __init__(self):
		self._counter = 0				
				
	def printButtonClickCounter(self):
		print("Counter:", self._counter)
		
	def wowButton(self):
		self._counter += 1
		print("You pressed the WOW button")
		self.printButtonClickCounter()

	def pacificButton(self):
		messages = [ "Go Boxers!", 
					"Now you owe $30,000", 
					"Wooo Forest Grove!",
					"Don't look back"]
		self._counter += 1
		print("You pressed the Pacific button")
		print ("\t",messages[self._counter % len(messages)] )
		self.printButtonClickCounter()


# a callback function does not need to be part of a class
def message():
	""" callback function to print OK when the button is pressed """
	print("OK")



handler = ButtonHandler()

# build the root
root = Tk()

# get a frame
cF = Frame(root)

# turn on the grid layout
cF.grid(column=0,row=0)

# create a button, hooked up the Frame, with the text OK
# and the button press goes to the function message()
okButton=Button(master=cF, text="OK",command=message)

# place the button the grid
okButton.grid(column=0,row=0)


# create a button, hooked up the Frame, with the text OK
# and the button press goes to the function message()
wowButton=Button(master=cF, text="Wow",command=handler.wowButton)

# place the button the grid
wowButton.grid(column=1,row=0)

# create a button, hooked up the Frame, with the text OK
# and the button press goes to the function message()
pacificButton=Button(master=cF, text="Pacific",command=handler.pacificButton)

# place the button the grid
pacificButton.grid(column=1,row=1)

# run the UI loop
root.mainloop()

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



def message():
	""" callback function to print OK when the button is pressed """
	print("OK")


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

# run the UI loop
root.mainloop()

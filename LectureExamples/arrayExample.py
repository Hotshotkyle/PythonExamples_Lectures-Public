#!/usr/bin/python3

################################
# File Name:    arrayExample.py
# Author:       Chadd Williams
# Date:         10/19/2016
# Class:        CS 360
# Assignment:   Lecture
# Purpose:      Demonstrate basic arrays
################################


import array

# an array must contain only one type of data.
theArray = array.array("i")
theArray.append(1)

print(theArray)
print(theArray[0])

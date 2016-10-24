#!/usr/bin/python3

########################################################################
# File Name:    test_doctest.py
# Author:       chadd williams
# Date:         Oct 23, 2016
# Class:        CS 360
# Assignment:   Example DocTest
# Purpose:      Show a simple set of DocTest tests
########################################################################

# invoke the tests via:  python3 test_doctest.py -v

"""
doctest Example

>>> sumTwo(2,2)
4
"""

def sumTwo(left, right) :
    """ return the sum of both values

    >>> sumTwo(1,2)
    3

    >>> sumTwo(1.1, 3)
    4.1
    """ 
    return left + right

if __name__ == "__main__":
    import doctest
    doctest.testmod()

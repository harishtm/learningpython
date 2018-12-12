#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
    Program to extract maximum numeric value from a given string
"""
import re

def extract_max_number(numstr):


    # \d+ is a regular expression which means
    # returns a list of string numbers
    numbers = re.findall('\d+', numstr)
    numbers = map(int, numbers) # Convert each number to int
    return max(numbers)

if __name__ == '__main__':
    
    numstr = input("Enter the string with numbers : ")
    print(extract_max_number(numstr))

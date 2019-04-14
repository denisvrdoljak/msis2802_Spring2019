#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 08:27:49 2018

@author: denisvrdoljak
"""

#triple quotes here let me space out the input message more easily
selectexamplemessage = """
select example to show:
    1. basic while loop
    2. while loop with if statement
    3. while loop, if with break
    4. while loop, if with continue

Make a selection (enter a number, or 'q' to quit):
""".strip() + " "
#

barn = ['cat','dog','elephant','giraffe']

menuoption = input(selectexamplemessage)
if menuoption.isnumeric():
    menuoption = int(menuoption)
elif menuoption+" "[0].lower() == 'q':
    print("quitting...")
    quit()
else:
    menuoption = 0
    #if something other than a vaid menu option is selected, set to 0
print("\n") #print a new line, space things out
if menuoption == 1:
    i=0
    # i is a counter that will help us iterate through the list
    # when i gets to the end of the list, the loop will stop
    while i < len(barn):
        print(barn[i] + " found in the barn")
        i += 1
        #increment counter
if menuoption == 2:
    i=0
    while i < len(barn):
        print(barn[i] + " found in the barn")
        i += 1

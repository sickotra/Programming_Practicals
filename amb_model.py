# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:40:21 2020

@author: shiva
"""
import random



y0 = 50    # Make a y variable
x0 = 50    # Make a x variable
print ("These are the original y0, x0 coods")
print (y0, x0) 


# Change y and x based on random numbers/ random walk 1 step.
if random.random() < 0.5:    #changed to 50 since 100 numbers now, checks half way
    y0 = y0 + 1
else: 
    y0 = y0 - 1
   
if random.random() < 0.5:
    x0 = x0 + 1
else: 
    x0 = x0 - 1

# Move this another step 
if random.random() < 0.5:
    y0 = y0 + 1
else: 
    y0 = y0 - 1
   
if random.random() < 0.5:
    x0 = x0 + 1
else: 
    x0 = x0 - 1    
print ("These are the y0, x0 after 2 steps")   
print (y0,x0) 




# Make a second set of y and xs, and make these change 
#randomly as well.
y1 = 50
x1 = 50
print ("These are the original y1, x1 coods")
print(y1, x1)

if random.random() < 0.5:  
    y1 = y1 + 1
else: 
    y1 = y1 - 1
   
if random.random() < 0.5:
    x1 = x1 + 1
else: 
    x1 = x1 - 1

#Move this another step
if random.random() < 0.5:
    y1 = y1 + 1
else: 
    y1 = y1 - 1
   
if random.random() < 0.5:
    x1 = x1 + 1
else: 
    x1 = x1 - 1
print ("These are the y1, x1 after 2 steps")  
print (y1, x1)

# Work out the distance between the two sets of y and xs.
#Dist worked out using pythagoras' theorem
y_diff = (y0 - y1)**2
x_diff = (x0 - x1)**2
yx_distance = (y_diff + x_diff)**0.5

print("This is the distance between coords")
print(yx_distance)


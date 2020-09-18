# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:40:21 2020

@author: shiva
"""
import random  #for random number generating
import operator #for extrating 2nd element of agents list
import matplotlib.pyplot #for plotting agents locations

agents = []     #Creates empty list to add sets of coords

#adds 1st set of coords to agents list, list inside a list
#agents[0][0] is the y coord..1st element of 1st element in 2D list
#agents[0][1] is the x coord..2nd element of 1st element in 2D list
agents.append([random.randint(0, 99),random.randint(0, 99)])  # y & x created randomly 0-99  
                         

# Change y and x based on random numbers/ random walk 1 step.
if random.random() < 0.5:    
    agents[0][0] = agents[0][0] + 1
else: 
    agents[0][0] = agents[0][0] - 1
   
if random.random() < 0.5:
    agents[0][1] = agents[0][1] + 1
else: 
    agents[0][1] = agents[0][1] - 1

# Move this another step 
if random.random() < 0.5:
    agents[0][0] = agents[0][0] + 1
else: 
    agents[0][0] = agents[0][0] - 1
   
if random.random() < 0.5:
    agents[0][1] = agents[0][1] + 1
else: 
    agents[0][1] = agents[0][1] - 1    



#Append a 2nd random set of y & x to the agents list
#Here y is agents[1][0]..1st element of 2nd element of 2d list
# x is agents[1][1]..2nd element of 2nd element of 2d list 
agents.append([random.randint(0, 99),random.randint(0, 99)])


if random.random() < 0.5:  
    agents[1][0] = agents[1][0] + 1
else: 
    agents[1][0] = agents[1][0] - 1
   
if random.random() < 0.5:
    agents[1][1] = agents[1][1] + 1
else: 
    agents[1][1] = agents[1][1] - 1

#Move this another step
if random.random() < 0.5:
    agents[1][0] = agents[1][0] + 1
else: 
    agents[1][0] = agents[1][0] - 1
   
if random.random() < 0.5:
    agents[1][1] = agents[1][1] + 1
else: 
    agents[1][1] = agents[1][1] - 1

print(agents) # 2D list of the 2 coords
#Work out the distance between the two sets of y and xs.
#Dist worked out using pythagoras' theorem
y_diff = (agents[0][0] - agents[1][0])**2
x_diff = (agents[0][1] - agents[1][1])**2
yx_distance = (y_diff + x_diff)**0.5

print("This is the distance between coords", yx_distance)

print(max(agents))   #gives max in the y direction

max_x = max(agents, key=operator.itemgetter(1))   #looks in the operator func to get max of 2nd element in the 2D list
                                                     #finds the max in the x direction
print(max_x)


#setting graph axis
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)

#plotting both points on a scatter graph, correct way ie x, y not y, x
matplotlib.pyplot.scatter(agents[0][1],agents[0][0])
matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
matplotlib.pyplot.scatter(max_x[1], max_x[0], color='red') #colours max in x direc red
matplotlib.pyplot.show()
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:40:21 2020

@author: shiva
This file contains an Agent class definition an some code to execute
"""

import random  #for random number generating
import operator #for extrating 2nd element of agents list
import matplotlib.pyplot #for plotting agents locations
import time #to see how long dist_between function takes to run

random.seed(0) #'fix' the random numbers so outputs stay constant
               #can change the seed arg anytime

def distance_between(a, b):
    """
    Calculate the distance between a and b using Pythagoras' and return it.
    The 2 dim is broken down now. When func called/used at bottom it works in 1st dim,
    This function is picking out elements in 2nd dim
    No need for any i index for loop etc as the args passed through already specify the agent used
 
    Parameters
    ----------
    a : List with 2 elements
        An arb agent with x, y coords
    b : List with 2 elements
        Another arb agent with x, y coors

    Returns
    -------
    number
        floating point 
    """
    y_diff = (a[0] - b[0])**2 #local variables
    x_diff = (a[1] - b[1])**2
    return (y_diff + x_diff)**0.5


num_of_agents = 10    #sets the no of agents
num_of_iterations = 100

agents = []     #Creates empty list to add sets of coords

#For Loop generating random coords between 0-99, for every agent
# then adding it to the agents list
for i in range (num_of_agents):
    agents.append ([random.randint(0, 99), random.randint(0, 99)])   
print("Initial Agents")
print (agents)
                        
# Change y and x for all agents based on random numbers/ random walk 1 step.
#agents[i][0] is the y coord of each agent/element in 2D list
#agents[i][1] is the x coord of each agent/element in 2D list
for j in range (num_of_iterations): 
    
    for i in range (num_of_agents):
        if random.random() < 0.5:    #random no between 0-1 to determine step
            agents[i][0] = (agents[i][0] + 1) % 100 #using torus boundary
        else: 
            agents[i][0] = (agents[i][0] - 1) % 100
   
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else: 
            agents[i][1] = (agents[i][1] - 1) % 100
print("Agents after Moving")
print (agents) # 2D list of all the agents/coord sets


print ("Max agent in y direction", max (agents))   #gives max in the y direc

#looks in operator func to get max of 2nd element in the 2D list, max in x dirc
max_x = max (agents, key=operator.itemgetter(1))   
print ("Max agent in x direction", max_x)



#Calling distance between agents function that was defined at top
#Unordered, end up with repeated combinations here & dist between coord and itself
max_between = None
min_between = None #initially setting to None so that max/min func can compare
start = time.perf_counter()

for m in range (0, num_of_agents, 1):     #1st loop starts by fixing 1st agent
    for k in range (m + 1, num_of_agents, 1):  #2nd loop runs through every other agent
        #if (m>k):
        print("m,k", m, k)
        distance = distance_between (agents[m], agents[k]) 
        print (distance)  #prints distances between agents
        
        if max_between is None:  #1st run will be true, so sets it to 1st dist
            max_between = distance 
        else:
            max_between = max (distance, max_between) #compare each new dist with 
                                                      #previous & update the max
        if min_between is None:
            min_between = distance 
        else:
            min_between = min (distance, min_between)
        #IS THERE A WAY TO CONDENSE THIS^?!

end = time.perf_counter()
print ("time = " + str (end - start))
print("Max distance between agents", max_between)
print("Min disctance between agents", min_between)



#setting graph axis
matplotlib.pyplot.ylim (0, 100)
matplotlib.pyplot.xlim (0, 100)

#plotting all points on a scatter graph, correct way ie x, y not y, x
for i in range (num_of_agents):
    matplotlib.pyplot.scatter (agents[i][1], agents[i][0])
    
matplotlib.pyplot.scatter (max_x[1], max_x[0], color='red') #colours max in x direc red
matplotlib.pyplot.show()
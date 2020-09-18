# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:40:21 2020

@author: shiva
This file contains an Agent class definition an some code to execute  NEED TO CHNAGE THIS!
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
     
    Take arguements a and b that are the 1st dimension of the agents list.
    Pick out elements in the 2nd dimension of agents list to calculate dist.
 
    Parameters
    ----------
    a : List with 2 integer elements
            An arb agent with x, y coords
    b : List with 2 integer elements
            Another arb agent with x, y coors

    Returns
    -------
    floating point number
        
    """
    
    y_diff = (a[0] - b[0])**2 #local variables
    x_diff = (a[1] - b[1])**2
    return (y_diff + x_diff)**0.5


num_of_agents = 10    #sets the no of agents
num_of_iterations = 100  #sets number of steps in the random walk

agents = []     #Creates empty list to add sets of coords

#For Loop generating random coords between 0-99, for every agent
# then adding it to the agents list
for i in range (num_of_agents):
    agents.append ([random.randint(0, 99), random.randint(0, 99)])   
print("Initial agents:")
print (agents)
                        
# Change y and x for all agents based on random numbers/ random walk 1 step
#agents[i][0] is the y coord of each agent/element in 2D list
#agents[i][1] is the x coord of each agent/element in 2D list
for j in range (num_of_iterations):  #moves coords num_of_iteration times
    
    for i in range (num_of_agents): #steps by 1 every agents y & x coord
        if random.random() < 0.5:    #random no between 0-1 to determine step
            agents[i][0] = (agents[i][0] + 1) % 100 #using torus boundary
        else: 
            agents[i][0] = (agents[i][0] - 1) % 100
   
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else: 
            agents[i][1] = (agents[i][1] - 1) % 100
print("Agents after moving", num_of_iterations, "times:")
print (agents) # 2D list of all the agents/coord sets


print ("Max agent in y direction:", max (agents))   #gives max in the y direc

#looks in operator func for max of 2nd element in the 2D list, max in x direc
max_x = max (agents, key = operator.itemgetter(1))   
print ("Max agent in x direction:", max_x)



#initially setting to None so that max/min dist func can compare
max_between = None 
min_between = None 

start = time.perf_counter() #start clock to assess efficiency 

##outer loop starts by fixing 1st agent stepping by 1 to last agent
for m in range (0, num_of_agents, 1):    
    
    #To optimise, run through only lower triangle of distances matrix,
    #where rows & cols are the agent, removing repeated combos and dists 
    #between an agent and itself
    for k in range (m + 1, num_of_agents, 1): 
        
        #find distance between 2 agents using defined function
        distance = distance_between (agents[m], agents[k]) 
        print (distance)  #prints distances between agents
        
        if max_between is None:  #1st run will be true, so sets it to 1st dist
            max_between = distance 
        else:
            #compare each new dist with previous & updates the max
            max_between = max (distance, max_between)
                                                  
        if min_between is None:
            min_between = distance 
        else:
            min_between = min (distance, min_between)
        #IS THERE A WAY TO CONDENSE THIS^?!

end = time.perf_counter() #end the timer for the calculating distances loops
print ("time = " + str (end - start))
print("Max distance between agents", max_between)
print("Min disctance between agents", min_between)



#setting graph axis
matplotlib.pyplot.ylim (0, 100)
matplotlib.pyplot.xlim (0, 100)

#plotting all points on a scatter graph, correct way ie x, y not y, x
for i in range (num_of_agents):
    matplotlib.pyplot.scatter (agents[i][1], agents[i][0])
    

matplotlib.pyplot.scatter (max_x[1], max_x[0], color='red') #max x red overlay
matplotlib.pyplot.show()  #displays scatter plot of agents
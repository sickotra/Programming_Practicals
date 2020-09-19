# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:40:21 2020

@author: shiva

This file contains an agent based model

"""

import random  #for random number generating
import operator #for extrating 2nd element of agents list
import matplotlib.pyplot #for plotting agents locations
import time #to see how long dist_between function takes to run
import agentframework #import the created module/class called Agent

#'fix' the random numbers so outputs stay constant, can change the seed arg
random.seed(0) 

def distance_between(a, b):
    """
    Calculate the distance between a and b using Pythagoras' and return it.
     
    Take arguements a and b that are the 1st dimension of the agents list.
    Pick out elements in the 2nd dimension of agents list, 
    using the Agents Class in agentframework module, to calculate dist.
 
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
    #create some local variables 
    y_diff = (a.y - b.y)**2 #difference between y coord of agents 
    x_diff = (a.x - b.x)**2 #difference between x coord of agents
    return (y_diff + x_diff)**0.5 



num_of_agents = 10    #sets the no of agents
num_of_iterations = 100  #sets number of steps in the random walk

agents = []     #Creates empty list to add sets of coords



'''#testing for 1 agent

agent_1 = agentframework.Agent() # WHAT WE WANT TO GET WORKING
#For the 1st agent, go to module agentframework and look in Agent Class. 
#agent_1 is an instance of the class Agent, ie. instantiate
#'agent_1' is what is passed in as 'self' 
 
#to test if it works, agent_1 is now acting as an object, can use . to call any
#functions inside the Class. 
print (agent_1.y, agent_1.x)   #will print the INITIAL 1st agent
                                                    
agent_1.move()     #calling the move func from class Agent
print (agent_1.y, agent_1.x)   #will print cood of 1st agent after 100 moves

#end of testing'''


print("Initialising agents--") 
#Generating random coords using Agent Class, for every agent
# then adding it to the agents list previously created
for i in range (num_of_agents): 
    agents.append (agentframework.Agent())      
    #arg not needed, the init method will initialise the agents using self
print ("Initial agents:")
print (agents)  #prints list of all initial agents 
                        

print ("Moving agents --")
# Change y and x for all agents using random walk
for j in range (num_of_iterations):   #moves the coords num_of_iteration times

    #Using the move func in Agents class on every coord set in the agents list
    for i in range (num_of_agents): 
        agents[i].move()                       
print("Agents after moving", num_of_iterations, "times:")
print (agents) # 2D list of all the agents/coord sets after stepping


#find max of objects in agents list by getting x, y attributes of the instances //I THINK?!
max_y = max (agents, key = operator.attrgetter('y')) #gives max in the y direc
max_x = max (agents, key = operator.attrgetter('x')) #gives max in the x direc
print ("Max agent in y direction:", max_y)   
print ("Max agent in x direction:", max_x)   


#finding distances between the agents
#initially setting to None so that max/min dist func can compare
max_between = None 
min_between = None 

start = time.perf_counter() #start clock to assess efficiency 

#outer loop starts by fixing 1st agent stepping by 1 to last agent
for m in range (0, num_of_agents, 1):    
    
    #To optimise time, run through only lower triangle of distances matrix,
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
print ("Max distance between agents", max_between)
print ("Min disctance between agents", min_between)



#setting graph axis
matplotlib.pyplot.ylim (0, 100)
matplotlib.pyplot.xlim (0, 100)

#plotting all points on a scatter graph, correct way ie x, y not y, x
for i in range (num_of_agents):
    #get ith obj from agents list, using Agents Class to specify x, y coords
    matplotlib.pyplot.scatter (agents[i].x, agents[i].y) 
    

matplotlib.pyplot.scatter (max_x.x, max_x.y, color='red') #max x red overlay
matplotlib.pyplot.scatter (max_y.x, max_y.y, color='blue')#max y dark blue 
matplotlib.pyplot.show()  #displays scatter plot of agents
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:40:21 2020

@author: shiva
"""
import random  #for random number generating
import operator #for extrating 2nd element of agents list
import matplotlib.pyplot #for plotting agents locations

num_of_agents = 10    #sets the no of agents
num_of_iterations = 100

agents = []     #Creates empty list to add sets of coords


#For Loop generating random coords between 0-99, for every agent
# then adding it to the agents list
for i in range (num_of_agents):
    agents.append ([random.randint(0, 99), random.randint(0, 99)])  
  
                        
# Change y and x for all agents based on random numbers/ random walk 1 step.
#agents[i][0] is the y coord of each agent/element in 2D list
#agents[i][1] is the x coord of each agent/element in 2D list
for j in range (num_of_iterations): 
    
    for i in range (num_of_agents):
        if random.random() < 0.5:    
            agents[i][0] = (agents[i][0] + 1) % 100 #using torus boundary
        else: 
            agents[i][0] = (agents[i][0] - 1) % 100
   
        if random.random() < 0.5:
            agents[i][1] = (agents[i][1] + 1) % 100
        else: 
            agents[i][1] = (agents[i][1] - 1) % 100

print (agents) # 2D list of all the agents/coord sets


'''Work out the distance between the two sets of y and xs.
Dist worked out using pythagoras' theorem
y_diff = (agents[0][0] - agents[1][0])**2
x_diff = (agents[0][1] - agents[1][1])**2
yx_distance = (y_diff + x_diff)**0.5

print("This is the distance between coords", yx_distance)'''



    
    
    

print ("Max in y direction", max (agents))   #gives max in the y direction

max_x = max (agents, key=operator.itemgetter(1))   #looks in the operator func to get max of 2nd element in the 2D list
                                                     #finds the max in the x direction
print ("Max in x direction", max_x)


#setting graph axis
matplotlib.pyplot.ylim (0, 100)
matplotlib.pyplot.xlim (0, 100)

#plotting all points on a scatter graph, correct way ie x, y not y, x
for i in range (num_of_agents):
    matplotlib.pyplot.scatter (agents[i][1], agents[i][0])
    
matplotlib.pyplot.scatter (max_x[1], max_x[0], color='red') #colours max in x direc red
matplotlib.pyplot.show()









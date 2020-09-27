# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 14:40:21 2020

@author: shiva

This file contains an agent based model.

"""

import random  #for random number generating
import operator #for extrating 2nd element of agents list
import matplotlib.pyplot #for plotting agents locations
from matplotlib.animation import FuncAnimation #for adding animation
import time #to see how long dist_between function takes to run
import agentframework #import the created module/class called Agent
import csv #to allow raster data to be read
import json #to write out python as a json file at end
import sys #to allow major model parameters to  be entered at command line

#'fix' the random numbers so outputs stay constant, can change the seed arg
random.seed(0) 



f = open ('in.txt', newline='') #read data from text file
#csv.reader gives data as list of list to be looped through
dataset = csv.reader (f, quoting=csv.QUOTE_NONNUMERIC) #convers no. to floats

environment = [] #empty list to add the rowlist elements (mutable)

for row in dataset:
    rowlist = [] #empty list to add each row as an element
    for value in row:
        rowlist.append (value) #adds each row's data as its own rowlist element
    environment.append (rowlist)  #each rowlist added to environ list, 2D now 
f.close() 	#file closed after reading data

#comment out belwo variables for command prompt interactivity
num_of_agents = 10    #sets the no of agents
num_of_iterations = 100  #sets number of steps in the random walk
neighbourhood = 20 #sets the neighbourhood 
# num_of_agents = int(sys.argv[1])    #User can input args from command prompt
# num_of_iterations = int(sys.argv[2]) 
# neighbourhood = int(sys.argv[3])  
print ("Number of Agents:", num_of_agents) #printint to show vals used
print ("Number of Iterations", num_of_iterations)
print ("Neighbourhood:", neighbourhood)

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



print ("Initialising agents--") 
#Generating random coords using Agent Class, for every agent
# then adding it to the agents list previously created

for i in range (num_of_agents): 
    
    #passing in data from our environ & agents list  
    agents.append (agentframework.Agent(environment, agents))
    #print (agents[i].agents)  #TEST to see each agent get agents list
#print ("Initial agents:") #comment out for large no's of agents
#print (agents)  #prints list of all initial agents
                        


print ("Moving agents", num_of_iterations, "times --")
# Change y and x for all agents using random walk

for j in range (num_of_iterations):   #moves the coords num of iteration times
    #randomly shuffles agents list each iternation, reduce model artifacts
    random.shuffle (agents) 
    for i in range (num_of_agents): #funcs act on every element in agents list
        agents[i].move() #caling move func in Agents class 
        agents[i].eat()  #shrink the environ for surrounding area of agents 
        #give each agent info about any nearby agents to share resources
        agents[i].share_with_neighbours (neighbourhood)                   
#print("Agents after moving:") #comment out for large no's of agents
#print (agents) # 2D list of agents after stepping



#find max of objects in agents list by getting x, y attributes of the instances
max_y = max (agents, key = operator.attrgetter('y')) #gives max in the y direc
max_x = max (agents, key = operator.attrgetter('x')) #gives max in the x direc
print ("Max agent in y direction (dark blue):", max_y)   
print ("Max agent in x direction (red):", max_x)   



#finding min/max distances between the agents
#initially setting to None so that max/min dist func can compare
max_between = None 
min_between = None 

start = time.perf_counter() #start clock to assess efficiency 
#outer loop starts by fixing 1st agent stepping by 1 to last agent
for m in range (0, num_of_agents, 1):    
    other_agent = agents[m]
    #To optimise run time, only lower triangle of distances matrix visited,
    #to remove repeated combos, where rows & cols are the agents 
    for k in range (m + 1, num_of_agents, 1): 
        #find distance between 2 agents using method
        distance = agents[k].distance_between(other_agent) 
        #print (distance)  #prints distances between agents, TEST- comment out
        if max_between is None:  #1st run will be true, so sets it to 1st dist
            max_between = distance 
        else:
            #compare each new dist with previous & updates the max
            max_between = max (distance, max_between)
                                                  
        if min_between is None:
            min_between = distance 
        else:
            min_between = min (distance, min_between)

end = time.perf_counter() #end the timer for the calculating distances loops
print ("time = " + str (end - start))
print ("Max distance between agents", max_between)
print ("Min distance between agents", min_between)




matplotlib.pyplot.ylim (0, 100) ##setting graph axis
matplotlib.pyplot.xlim (0, 100)
#display environ data as an image, dark blue markings = eaten environ
matplotlib.pyplot.imshow(environment) 
                                        
#plotting all points on a scatter graph, correct way ie x, y not y, x
for i in range (num_of_agents):
    #get ith obj from agents list, using Agents Class to specify x, y coords
    matplotlib.pyplot.scatter (agents[i].x, agents[i].y) 
    
matplotlib.pyplot.scatter (max_y.x, max_y.y, color='blue')#max y dark blue overlay
matplotlib.pyplot.scatter (max_x.x, max_x.y, color='red') #max x red overlay
matplotlib.pyplot.show()  #displays scatter plot of agents



#Animation
fig = matplotlib.pyplot.figure(figsize=(7, 7)) #create a figure and set axes
ax = fig.add_axes([0, 0, 1, 1])
ax.set_autoscale_on(False)

carry_on = True #initially set to true

def update(frame_number):
    """Move and plot agents, stop if the store value reaches 1000.""" 
          
    fig.clear()
    global carry_on #so variable can be assigned in the func
    
    for i in agents: 
        i.move() #move method for each agent
        
    #if random.random() < 0.1:
    if i.store >= 1000: #stops eating once store val reaches 999
        carry_on = False
        print ("stopping condition reached")
    
    for i in agents:  #for every agent in the agents list
        matplotlib.pyplot.scatter(i.x, i.y) #plot x,y of each agent
        print (i.x, i.y)   
        

def gen_function (b= [0]): 
    """
    Stop supplying an input when condition is met.
    
    The function will stop yielding a result once it has provided an output
    num_of_iteration times and when store value is over 1000.

    Parameters
    ----------
    b : list, optional
        The default is [0].

    Yields
    ------
    a : int

    """
   
    a = 0 #initially set a to 0
    #when a is < num of iter & carry_on is True, gives a
    while (a < num_of_iterations) & (carry_on): 
        yield a
        a = a + 1 #add 1 to a 

#Create the animation using update func and frames arg is the gen func        
animation = FuncAnimation(fig,update, interval=1, repeat=False, frames=gen_function)
matplotlib.pyplot.show() #shows the animation created in a pop up window







#outputting environment data as a json file
#f = open ('out.json', 'w') #create json file called 'out', write mode
#json.dump (environment, f) #dump 2D environ list data into the json file 'out'
#f.close() #close json file



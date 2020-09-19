# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 23:01:03 2020

@author: shiva

This file contains an Agent class definition and some code to execute

"""

import random   #for random number generating


class Agent: #creating our class for Agent, so when it is used in main, will go through here 

    #the init (initialiser) method, used to set new self object's attributes to their initial state
    def __init__(self): #the agent specified is passed in, atm agent_1
        self.y = random.randint(0, 99) #instance variables to randomise initial y, x coords, between 0-99, for the particular agent
        self.x = random.randint(0, 99)  #initialising agents!!!!
    
    
    #the move method, steps by 1 every agents y & x coords
    def move(self):
        if random.random() < 0.5:    #random no between 0-1 to determine step
            #using self.y/x now bc there's no 'agents' list to look into in this eviromnet anymore
            #so dont need to use index in a for loop to determine the agent we are using//1st agent, agent_1 
            #is already specified here.
            self.y = (self.y + 1) % 100 #TODO, understand using torus boundary
        else: 
            self.y = (self.y - 1) % 100 #TODO, CHNAGE THIS TO FOR LOOP ITERATOR STYLE,P5
   
        if random.random() < 0.5:
            self.x = (self.x + 1) % 100 #whatever self is, ie whatever variable name/object of individual agent is called in the main will have its x coord stepped
        else: 
            self.x = (self.x - 1) % 100
    
    def __repr__(self):  #repr function makes printable version of the object, cant directly print objs as they are mutable?
        return str([self.x, self.y]) #used to print list of initial & moved agents
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 23:01:03 2020

@author: shiva

This file contains an Agent class definition and some code to execute

"""

import random   #for random number generating


class Agent: #creating our class, template for every agent 
    #protecting _x,_y hidden variables, when y, x is accessed/mutated in model,
    #will divert to these
    def get_y (self):
        return self._y 
    def get_x (self):
        return self._x  
    def set_y (self, value):
        self._y = value
    def set_x (self, value):
        self._x = value 
    #given the x, y property attribues and docstrings
    y = property (get_y, set_y, "I'm the 'y' property") 
    x = property (get_x, set_x, "I'm the 'x' property")


    #init constructor method to set new instance object's attributes to their initial state
    #the agent is passed in & all MUTABLE environ list data
    #environ for all agents will change when  .envi is used for the specified agent, since the environ list is mutable
    def __init__(self, environment):  #e.g agent_1 as self & all data from envi list// 
        self._y = random.randint(0, 99) #instance variables to randomise initial y, x coords, between 0-99, for the particular agent
        self._x = random.randint(0, 99)  #initialising agents!!!!
        self.environment = environment #instance var to let every agent have access to the environ data
        self.store = 0    #not explained yet
    
    def __repr__(self):  #repr function makes printable version of the object, cant directly print objs as they are mutable?
        return str([self._x, self._y]) #used to print list of initial & moved agents
    
    #the move method, steps by 1 every agents y & x coords
    def move(self):
        if random.random() < 0.5:    #random no between 0-1 to determine step
            #using self.y/x now bc there's no 'agents' list to look into in this eviromnet anymore
            #so dont need to use index in a for loop to determine the agent we are using//1st agent, agent_1 
            #is already specified here.
            self._y = (self._y + 1) % 100 #TODO, understand using torus boundary
        else: 
            self._y = (self._y - 1) % 100 #TODO, CHNAGE THIS TO FOR LOOP ITERATOR STYLE,P5
   
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100 #whatever self is, ie whatever variable name/object of individual agent is called in the main will have its x coord stepped
        else: 
            self._x = (self._x - 1) % 100
    
    def eat(self):
        if self.environment[self._y][self._x] > 10: #if the main environment for that particular agent is >10, then minus 10 and add it to the 'store'
            self.environment[self._y][self._x] -= 10
            self.store += 10


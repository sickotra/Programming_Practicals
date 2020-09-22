# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 23:01:03 2020

@author: shiva

This file contains an Agent class definition and some code to execute.

"""

import random   #for random number generating


class Agent:

    #creating our class, template for every agent 
    #protecting _x,_y hidden variables #DOC STRING NEEDED HERE TOO!!!!

    def get_y (self):
        """Divert access of y int variable to a hidden int variable."""
        return self._y
    
    def get_x (self):
        """Divert access of x int variable to a hidden int variable."""
        return self._x  
    
    def set_y (self, value):
        """Divert mutation of y int variable to a hidden int variable."""
        self._y = value
        
    def set_x (self, value):
        """Divert access of x int variable to a hidden int variable."""
        self._x = value 
    #given the y, x property attribues and docstrings
    y = property (get_y, set_y, "I'm the 'y' property") 
    x = property (get_x, set_x, "I'm the 'x' property")


    def __init__(self, environment, agents):
        """
        Construct the initial attribute states of the instance object.
        
        Parameters
        ----------
        environment : List.
            2D containing lists of the agents y,x coords. 

        Returns
        -------
        Agent.

        """
        #Randomising initial y, x coords of the agent to ints between 0-99
        self._y = random.randint(0, 99) #instance variables created
        self._x = random.randint(0, 99)  
        #Giving every agent access to the same environment data
        self.environment = environment 
        #Creating a 'store' for the environment thats been eaten
        self.store = 0 #inital store begins at zero and will increase later
        self.agents = agents #giving every agent access to the 'agents' list
    
    def __repr__(self):
        """Make printable string version of the instance objects in agent list."""
        
        return str([self._x, self._y]) #used to print initial & moved agents
    
    
    def move(self):
        """Random walk 1 step for every agents x, y coords."""
        
        #Moving both x, y coord by 1 step with equal probablity.
        #If generated random number is less than 1/2, step by +1, otherwise
        #step by -1.
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100 #using torus boundary
        else: 
            self._y = (self._y - 1) % 100 #TODO, CHANGE TO FOR LOOP ITERATOR STYLE,P5
   
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else: 
            self._x = (self._x - 1) % 100
    
    
    def eat(self):
        """Shrink the data in the environment 2D list and add to a store."""
        
        #If main environment is >10, minus 10 and add it to the 'store'.
        #Environ for all agents will change, since list is mutable.
        if self.environment[self._y][self._x] > 10: 
            self.environment[self._y][self._x] -= 10
            self.store += 10
        #Need an else?
        
    def distance_between(self, other_agent):
        """
        Calculate the distance between a and b using Pythagoras' and return it.
         
        Take arguements a and b that are the 1st dimension of the agents list.
        Pick out elements in the 2nd dimension of agents list, 
        using the Agents Class in agentframework module, to calculate dist.
     
        Parameters
        ----------
        a : List
                An arb agent with int x, y coords.
        b : List 
                An arb agent with int x, y coords.
    
        Returns
        -------
        Float.    #UPDATE THE DOC STRING FOR OOP
            
        """
        
        #create some local variables 
        y_diff = (self.y - other_agent.y)**2 #difference between y coord of agents 
        x_diff = (self.x - other_agent.x)**2 #difference between x coord of agents
        return (y_diff + x_diff)**0.5 
        

    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum/2 
                self.store = ave
                agent.store = ave
                #print ("sharing" + str(dist) + " " + str(ave))
        
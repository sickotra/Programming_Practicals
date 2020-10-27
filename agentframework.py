# -*- coding: utf-8 -*-
"""
Programming for Social Science.
Agent Class definition and code to execute.

Created on Fri Sep 18 23:01:03 2020
@author: Shivani Sickotra

"""

import random   #for random number generating


class Agent:
    """
    Agent Class:
        A class to give attributes and behaviours to an abstract agent.
        
    Constructor arguements:
        environment -- 2D list containing coords agents will interact with.
        agents -- a list of all the agents in the environment.
        y -- y coord before init method sets agent's coods.
        x -- x coord before init method sets agent's coods.
    
    Agent characteristics:
        - store
        - y coordinate
        - x coordinate 
        
    Agent behaviours:
        - move
        - eat
        - calculate distance between itself and another agent
        - share resources with neighbours
     
    """
    
    #creating our class, template for every agent 
    #protecting _x,_y hidden variables           

    def get_y (self):
        """Divert access of y int variable to a hidden int variable."""
        return self._y
    
    def get_x (self):
        """Divert access of x int variable to a hidden int variable."""
        return self._x  
    
    def set_y (self, value):
        """Divert mutation of y int variable to a hidden float variable."""
        self._y = value
        
    def set_x (self, value):
        """Divert mutation of x int variable to a hidden float variable."""
        self._x = value 
    #given the y, x property attribues and docstrings
    y = property (get_y, set_y, "I'm the 'y' property") 
    x = property (get_x, set_x, "I'm the 'x' property")


    def __init__(self, environment, agents, y = None, x = None):
        """
        Construct the initial attribute states of the instance object.
        
        Parameters
        ----------
        environment : list.
            2D containing lists of row data from imported file 'in.txt'. 
        agents : list.
            2D containing lists of all the agents y,x coords.
        y : NoneType, optional
            The default is None.
        x : NoneType, optional
            The default is None.

        Returns
        -------
        Agent.

        """
        
        #Randomising initial y, x coords of the agent to ints between 0-299
        #if no y, x given, otherwise use data parsed in from HTML webpage
        if (y == None):
            self._y = random.randint(0, 299) 
        else:
            self._y = y
            
        if (x == None):
            self._x = random.randint(0, 299)  
        else:
            self.x = x
            
        #Giving every agent access to the same environment data
        self.environment = environment 
        #Creating a 'store' for the environment thats been eaten
        self.store = 0 #inital store begins at zero and will increase later
        self.agents = agents #giving every agent access to the 'agents' list
       
    
    def __repr__(self):
        """Make printable string version of instance objects in agent list."""
        
        return str([self._x, self._y]) #used to print initial & moved agents
    
    
    def move(self):
        """Random walk 1 step for every agents x, y coords."""
        
        #Moving both x, y coord by 1 step with equal probablity.
        #If generated random number is less than 1/2, step by +1, otherwise
        #step by -1.
        if random.random() < 0.5:
            self._y = (self._y + 1) % 300 #using torus boundary
        else: 
            self._y = (self._y - 1) % 300 
   
        if random.random() < 0.5:
            self._x = (self._x + 1) % 300
        else: 
            self._x = (self._x - 1) % 300
    
    
    def eat(self):
        """Shrink the data in the environment 2D list and add to a store."""
        
        #If main environment is >10, minus 10 and add it to the 'store'.
        #Environ for all agents will change, since list is mutable.
        if self.environment[self._y][self._x] > 10: 
            self.environment[self._y][self._x] -= 10
            self.store += 10
               
        
    def distance_between(self, other_agent):
        """
        Calculate distance between 2 agents using Pythagoras' and return it.
        
        Parameters
        ----------
        other_agent : Agent.
                An arb agent with int x, y coords.
    
        Returns
        -------
        float.
            
        """
    
        y_diff = (self._y - other_agent.y)**2 #diff between y coord of agents 
        x_diff = (self._x - other_agent.x)**2 #diff between x coord of agents
        return (y_diff + x_diff)**0.5 
        

    def share_with_neighbours(self, neighbourhood):
        """
        
        Share resources to other agents in close range.
        
        If distance to other agents is less than or equal to the neighbourhood 
        int value, then share resources by setting its own and the neighbours' 
        stores to the average of the store between them.

        
        Parameters
        ----------
        neighbourhood : int.
            The variable to choose when the resources will be shared.

        Returns
        -------
        None.

        """
        
        for i in self.agents: #for every agent in the agents list
            dist = self.distance_between(i) #dist between this agent & another
            
            if dist <= neighbourhood: #dist less then or equal to integer set
                average = (self.store + i.store)/2  #calulate average of stores
                self.store = average #set both stores to new average 
                i.store = average 
                #print ("sharing" + str(dist) + " " + str(average))  #TEST
        

            
        



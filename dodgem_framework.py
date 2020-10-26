# -*- coding: utf-8 -*-
"""
Programming for Social Science.
Dodgem Class definition and code to execute.

Created on Fri Sep 18 23:01:03 2020
@author: Shivani Sickotra

"""

import random   #for random number generating


class Dodgem:
    """
    Dodgem Class:
        A class to give attributes and behaviours to an abstract dodgem.
        
    Constructor arguements:
        arena -- 2D list containing coords dodgems will interact with.
        dodgems -- a list of all the dodgems in the arena.
        y -- y coord before init method sets dodgems' coods.
        x -- x coord before init method sets dodgmes' coods.
    
    Dodgem characteristics:
        - electricity store
        - damage store
        - y coordinate
        - x coordinate 
        
    Dodgem behaviours:
        - move
        - power
        - calculate distance between itself and another dodgem
        - share resources/electricity with neighbours
     
    """
    
    #creating our class, template for every dodgem
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


    def __init__(self, arena, dodgems, y = None, x = None):
        """
        Construct the initial attribute states of the instance object.
        
        Parameters
        ----------
        arena : list.
            2D containing lists of row data from imported file 'in.txt'. 
        dodgems : list.
            2D containing lists of all the dodgems y,x coords.
        y : NoneType, optional
            The default is None.
        x : NoneType, optional
            The default is None.

        Returns
        -------
        Dodgem.

        """
        
        #Randomising initial y, x coords of the dodgem to ints between 0-299
        #if no y, x given, otherwise use data parsed in from HTML webpage
        if (y == None):
            self._y = random.randint(0, 299) 
        else:
            self._y = y
            
        if (x == None):
            self._x = random.randint(0, 299)  
        else:
            self.x = x
            
        #Giving every dodgem access to the same arena data
        self.arena = arena
        #Creating an 'electricity store' for the elec taken from arena
        self.elec_store = 30 #inital store begins at 30 and will increase later
        self.dodgems = dodgems #giving every dodgem access to the 'dodgems' list
        self.damage = 0 #initial damage is 0 and increases after bumping others
       
    
    def __repr__(self):
        """Make printable string version of instance objects in dodgems list."""
        
        return str([self._x, self._y]) #used to print initial & moved dodgems
    
    
    def move(self):
        """Random walk 1 step for every dodgems x, y coords."""
        
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
    
    
    def power(self):  #TODO chnaged eat name
        """Deplete arena electricity and add it to the dodgem electricity store."""
        
        #If main arena is >10, minus 10 and add it to the 'electricity store'.
        #Arena for all agents will change, since list is mutable.
        if self.arena[self._y][self._x] > 10: 
            self.arena[self._y][self._x] -= 10
            self.elec_store += 10
               
        
    def distance_between(self, other_dodgem):
        """
        Calculate distance between 2 dodgems using Pythagoras' and return it.
        
        Parameters
        ----------
        other_dodgem : Dodgem.
                An arb dodgem with int x, y coords.
    
        Returns
        -------
        float.
            
        """
    
        y_diff = (self._y - other_dodgem.y)**2 #diff between y coord of dodgems 
        x_diff = (self._x - other_dodgem.x)**2 #diff between x coord of dodgems
        return (y_diff + x_diff)**0.5 
        

    def share_with_neighbours(self, neighbourhood):
        """
        
        Share electricty resources with other dodgems in close range.
        
        If distance to other dodgems is less than or equal to the neighbourhood 
        int value, then share electricty by setting its own and the neighbours' 
        electricty stores to the average of the store between them.

        
        Parameters
        ----------
        neighbourhood : int.
            The variable to choose when the resources will be shared.

        Returns
        -------
        None.

        """
        
        for i in self.dodgems: #for every dodgem in the dogems list
            dist = self.distance_between(i) #dist between this dodgem & another
            
            if dist <= neighbourhood: #dist less then or equal to integer set
                average = (self.elec_store + i.elec_store)/2  #calulate average of stores
                self.elec_store = average #set both stores to new average 
                i.elec_store = average 
                #print ("sharing" + str(dist) + " " + str(average))  #TEST
    

    #NEW COLLIDE METHOD 
    def collide(self):
        
        for i in self.dodgems: #for every dodgem in the dogems list
            dist = self.distance_between(i) #dist between this dodgem & another
            
            if dist == 0: #if dist is 0 ie. 2 dodgems collided, increase damage
                self.damage = self.damage + 5  #every collision adds 5 to damage
                #print(self.damage)
                
                #FIXME ANOTHER WAY TO REMOVE FROM LIST?? 
                #self.dodgems = [dodgem for dodgem in self.dodgems if self.damage < 50]

            

                
        



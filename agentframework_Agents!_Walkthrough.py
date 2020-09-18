# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:57:33 2020

@author: agdtu
"""
import random

class Agent:
    
    def __init__(self):
        self.y = random.randint(0,99)
        self.x = random.randint(0,99)
        
    def move(self):
        if random.random() < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100

        if random.random() < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
        
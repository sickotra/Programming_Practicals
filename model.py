# -*- coding: utf-8 -*-
"""
Programming for Social Science.
Agent based model.

Created on Tue Sep 15 14:40:21 2020
@author: Shivani Sickotra

"""

import random  #for random number generating
import operator #for extrating 2nd element of agents list
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot #for plotting agents locations
from matplotlib.animation import FuncAnimation #for adding animation
import time #to see how long dist_between function takes to run
import agentframework #import the created module/class called Agent
import csv #to allow raster data to be read
import json #to write out python as a json file at end
import sys #to allow major model parameters to  be entered at command line
import requests #to download webpage data
import bs4 #to process webpage

#'fix' the random numbers so outputs stay constant, can change the seed arg
random.seed(0) 



#Web scraping 
#download the HTML page with data, no username/password needed
url = 'http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html'
r = requests.get(url)
content = r.text #to get page, assign data as a variable

#take content from the request obj and parse it into the DOM 
#can use soup obj to navigate/search around data
soup = bs4.BeautifulSoup(content, 'html.parser')

#use soup to get all table elements with attribute y & x
tdy = soup.find_all(attrs = {"class": "y"})
tdx = soup.find_all(attrs = {"class": "x"})
print (tdy) #print the y's and x's
print(tdx)



#Setting up environment 
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



#Allowing command line arguments
#if 4 args are not given at command line (1st arg is model.py file name)
if len (sys.argv) != 4: 
    
    if len (sys.argv) == 1: #if only 1 arg file name is entered
        print('Model args not provided - running for default args')
    else:
        print ('Number of args incorrect - running for default agrs')
    num_of_agents = 10    #sets the default no of agents
    num_of_iterations = 100  #sets default number of steps in the random walk
    neighbourhood = 20 #sets the default neighbourhood value 

else:
    try:
        num_of_agents = int(sys.argv[1])  #User can input args from command prompt
        num_of_iterations = int(sys.argv[2]) 
        neighbourhood = int(sys.argv[3])  
        print ('Running for args entered')
    except:
        str (sys.argv[1:]) #does not allow characters as variable args
        print ('Wrong arg type entered - use only integers')
 
print ("Number of Agents:", num_of_agents) #print to show vals used
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
    
    y = int (tdy[i].text)
    x = int (tdx[i].text)
    #passing in data from our environ & agents list and y,x 
    agents.append (agentframework.Agent(environment, agents, y, x))
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



#Find max of objects in agents list by getting x, y attributes of the instances
max_y = max (agents, key = operator.attrgetter('y')) #gives max in the y direc
max_x = max (agents, key = operator.attrgetter('x')) #gives max in the x direc
print ("Max agent in y direction (square dark blue):", max_y)   
print ("Max agent in x direction (square red):", max_x)   



#Finding min/max distances between the agents
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
print ("Max distance between agents", max_between)
print ("Min distance between agents", min_between)
print ("Time taken to calculate distance between agents = " + str (end - start))


#Plotting the agents 
matplotlib.pyplot.ylim (0, 100) ##setting graph axis
matplotlib.pyplot.xlim (0, 100)
matplotlib.pyplot.title ('A plot to show the agents locations & interactions within the environment')
matplotlib.pyplot.xlabel('x')
matplotlib.pyplot.ylabel('y')
#display environ data as an image, dark blue markings = eaten environ
matplotlib.pyplot.imshow(environment) 
                                        
#plotting all points on a scatter graph, correct way ie x, y not y, x
for i in range (num_of_agents):
    #get ith obj from agents list, using Agents Class to specify x, y coords
    matplotlib.pyplot.scatter (agents[i].x, agents[i].y) 
  
#max y dark blue overlay & max x red overlay, square markers    
matplotlib.pyplot.scatter (max_y.x, max_y.y, color='blue', marker=(','))
matplotlib.pyplot.scatter (max_x.x, max_x.y, color='red', marker=(',')) 
matplotlib.pyplot.show()  #displays scatter plot of agents



#Animation
fig = matplotlib.pyplot.figure(figsize=(7, 7)) #create a figure and set axes
ax = fig.add_axes([0, 0, 1, 1])
ax.set_autoscale_on(False)

carry_on = True #initially set to true

def update(frame_number):
    """Move and plot agents, stop if the store value reaches 1200.""" 
          
    fig.clear()
    global carry_on #so variable can be assigned in the func
    
    for i in agents: 
        i.move() #move method for each agent
        
    #if random.random() < 0.1:
    if i.store >= 1200: #stops eating once store val reaches 1199
        carry_on = False
        print ("stopping condition reached")
    
    for i in agents:  #for every agent in the agents list
        matplotlib.pyplot.title ('Animation to show movement of agents')
        matplotlib.pyplot.xlabel('x')
        matplotlib.pyplot.ylabel('y')
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


def run ():
    """ Run the animation using the update function and display this."""
    
    animation = FuncAnimation(fig, update, interval=1, repeat=False, frames=gen_function)
    canvas.show() #shows animation in Figure 2 when model is ran from the menu command



#Creating GUI 
root = tkinter.Tk() #build main window
root.wm_title ("Model") #sets title for main window
#create a matplotlib canvas within main window and associate with fig 
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master = root) 
#pack lays out onto the window
canvas._tkcanvas.pack(side = tkinter.TOP, fill = tkinter.BOTH, expand = 1) 

menu_bar = tkinter.Menu(root) #create menu, passing in the root window
root.config(menu = menu_bar) #config root so that its menu is the menu created
model_menu = tkinter.Menu (menu_bar)
menu_bar.add_cascade (label = "Model", menu = model_menu) #add menu as dropdown
model_menu.add_command (label = "Run model", command = run) #bind run func 
tkinter.mainloop()



#Outputting environment data as a json file
f = open ('out.json', 'w') #create json file called 'out', write mode
json.dump (environment, f) #dump 2D environ list data into the json file 'out'
f.close() #close json file



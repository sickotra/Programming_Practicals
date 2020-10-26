# -*- coding: utf-8 -*-
"""
Programming for Social Science.
Agent based model - Dodgy Dodgems.

Created on Tue Sep 15 14:40:21 2020
@author: Shivani Sickotra

"""

# Import packages needed to run
import random  #for random number generating
import operator #for extrating 2nd element of dodgems list
import tkinter #for GUI 
import matplotlib #for plotting
matplotlib.use('TkAgg')
import matplotlib.pyplot #for plotting dodgem locations
from matplotlib.animation import FuncAnimation #for adding animation
import time #to see how long dist_between function takes to run
import dodgem_framework #import the created module/class called Dodgems
import csv #to allow raster data to be read
import json #to write out python as a json file at end
import sys #to allow major model parameters to  be entered at command line
import requests #to download webpage data
import bs4 #to process webpage

#'fix' the random numbers so outputs stay constant, can change the seed arg
random.seed(0) 



# Web scraping 
# Download the HTML page with data, no username/password needed
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



# Setting up arena 
f = open ('in.txt', newline='') #read data from text file
#csv.reader gives data as list of list to be looped through
dataset = csv.reader (f, quoting=csv.QUOTE_NONNUMERIC) #convers no. to floats

arena = [] #empty list to add the rowlist elements (mutable)

for row in dataset:
    rowlist = [] #empty list to add each row as an element
    for value in row:
        rowlist.append (value) #adds each row's data as its own rowlist element
    arena.append (rowlist)  #each rowlist added to arena list, 2D now 
f.close() 	#file closed after reading data



# Allowing command line arguments
#if 4 args are not given at command line (1st arg is dodgems_model.py file name)
if len (sys.argv) != 4: 
    
    if len (sys.argv) == 1: #if only 1 arg file name is entered
        print('Model args not provided - running for default args')
    else:
        print ('Number of args incorrect - running for default agrs')
    num_of_dodgems = 10    #sets the default no of agents
    num_of_iterations = 100  #sets default number of steps in the random walk
    neighbourhood = 20 #sets the default neighbourhood value 

else:
    try:
        num_of_dodgems = int(sys.argv[1])  #User can input args from cmd prompt
        num_of_iterations = int(sys.argv[2]) 
        neighbourhood = int(sys.argv[3])  
        print ('Running for args entered')
    except:
        str (sys.argv[1:]) #does not allow characters as variable args
        print ('Wrong arg type entered - use only integers')
 
print ("Number of Dodgems:", num_of_dodgems) #print to show vals used
print ("Number of Iterations", num_of_iterations)
print ("Neighbourhood:", neighbourhood)



dodgems = []     #Creates empty list to add sets of coords

print ("Initialising dodgems--") 
# Generating random coords using Dodgem Class, for every dodgem
# then adding it to the dodgems list previously created

for i in range (num_of_dodgems): 
    
    y = int (tdy[i].text)#reading in table data x, y as string, convert to int 
    x = int (tdx[i].text) 
    #passing in data from our arena & dodgems list and y,x 
    dodgems.append (dodgem_framework.Dodgem(arena, dodgems, y, x))
    #print (dodgems[i].dodgems)  #TEST to see each dodgem get dodgems list
#print ("Initial dodgems:") #comment out for large no's of dodgems
#print (dodgems)  #prints list of all initial dodgems
                        


print ("Moving dodgems for", num_of_iterations, "seconds --")
# Change y and x for all dodgems using random walk

for j in range (num_of_iterations):   #moves the coords num of iteration times
    #randomly shuffles dodgems list each iternation, reduce model artifacts
    random.shuffle (dodgems) 
    for i in range (num_of_dodgems): #funcs act on every element in dodgems list
        dodgems[i].move() #caling move func in Dodgems class 
        dodgems[i].power()  #deplete arena electricity and add to dodgem 
        #give each dodgem info about any nearby dodgems to share resources
        dodgems[i].share_with_neighbours (neighbourhood) 
        dodgems[i].collide()                  
#print("Dodgems after moving:") #comment out for large no's of dodgems
#print (dodgems) # 2D list of dodgems after stepping


#FIXME TRY AND REMOVE DODGEMS FROM LIST 

# working_dodgems = dodgems[:]
# for j in range (num_of_iterations):
#     for i in range (num_of_dodgems):
#         if working_dodgems[i].damage >= 50: #if damage is above 50, remove/shut down the dodgem
#             working_dodgems.remove(i)
# print(working_dodgems)   
    
# for n in dodgems[:]:#loop through a copy/complete slice of the list, so that no objects are missed
#     if dodgems[n].damage >= 50: #if damage is above 50, remove/shut down the dodgem
#         dodgems.remove(dodgems[n]) 
# print(dodgems)




#Find max of objects in dodgems list by getting x, y attributes of the instances
max_y = max (dodgems, key = operator.attrgetter('y')) #gives max in the y direc
max_x = max (dodgems, key = operator.attrgetter('x')) #gives max in the x direc
print ("Max agent in y direction (square dark blue):", max_y)   
print ("Max agent in x direction (square red):", max_x)   



# Finding min/max distances between the dodgems
#initially setting to None so that max/min dist func can compare
max_between = None 
min_between = None 

start = time.perf_counter() #start clock to assess efficiency 
#outer loop starts by fixing 1st agent stepping by 1 to last dodgem
for m in range (0, num_of_dodgems, 1):    
    other_dodgem = dodgems[m]
    #To optimise run time, only lower triangle of distances matrix visited,
    #to remove repeated combos, where rows & cols are the dodgems
    for k in range (m + 1, num_of_dodgems, 1): 
        #find distance between 2 dodgems using method
        distance = dodgems[k].distance_between(other_dodgem) 
        #print (distance)  #prints distances between dodgem, TEST- comment out
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
print ("Max distance between dodgems", max_between)
print ("Min distance between dodgems", min_between)
print ("Time taken to calculate distance between dodgems = " + str (end - start))



# Plotting the dodgems 
matplotlib.pyplot.ylim (0, 300) #setting graph axis
matplotlib.pyplot.xlim (0, 300)
matplotlib.pyplot.title ('A plot to show the dodgems locations')
matplotlib.pyplot.xlabel('x')
matplotlib.pyplot.ylabel('y')
#display arena data as an image, dark blue markings = electricity depleted from arena
matplotlib.pyplot.imshow(arena) 
#figure caption
txt= "Fig 1. End locations of " + str(num_of_dodgems) + " dodgems in the arena after " + str(num_of_iterations) + " seconds"
matplotlib.pyplot.figtext(0.5, 0.01, txt, wrap=True, horizontalalignment='center', fontsize=8)

                                        
# Plotting all points on a scatter graph, correct way ie x, y not y, x
for i in range (num_of_dodgems):
    #get ith obj from dodgems list, using Dodgem Class to specify x, y coords
    matplotlib.pyplot.scatter (dodgems[i].x, dodgems[i].y) 
  
#max y dark blue overlay & max x red overlay, square markers    
matplotlib.pyplot.scatter (max_y.x, max_y.y, color='blue', marker=(','))
matplotlib.pyplot.scatter (max_x.x, max_x.y, color='red', marker=(',')) 
matplotlib.pyplot.show()  #displays scatter plot of dodgems



# Animation
fig = matplotlib.pyplot.figure(figsize=(7, 7)) #create a figure and set axes
ax = fig.add_axes([0, 0, 1, 1])
ax.set_autoscale_on(False)

carry_on = True #initially set to true

def update(frame_number):
    """Move and plot dodgems, stop if the electricity store value reaches 1200."""
          
    fig.clear()
    global carry_on #so variable can be assigned in the func
    
    for i in dodgems: 
        i.move() #move method for each dodgem
        
    #if random.random() < 0.1:
    if i.elec_store >= 1200: #stops once electricty store val reaches 1199, overpowered
        carry_on = False
        print ("Dodgems overpowered")  
    
    
    for i in dodgems:  #for every dodgem in the dodgems list
        matplotlib.pyplot.title ('Animation to show movement of dodgems')
        matplotlib.pyplot.xlabel('x')
        matplotlib.pyplot.ylabel('y')
        matplotlib.pyplot.scatter(i.x, i.y) #plot x,y of each dodgem
        #print (i.x, i.y)   #to test if working 
        

def gen_function (b= [0]): 
    """
    Stop supplying an input when condition is met.
    
    The function will stop yielding a result once it has provided an output
    num_of_iteration times and when store value is 0.

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
    
    animation=FuncAnimation(fig, update, interval=1, repeat=False, frames=gen_function)
    canvas.show() #shows animation in Figure 2 when model is ran from the menu command



# Creating GUI 
root = tkinter.Tk() #build main window
root.wm_title ("Dodgems Model") #sets title for main window
#create a matplotlib canvas within main window and associate with fig 
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master = root) 
#pack lays out onto the window
canvas._tkcanvas.pack(side = tkinter.TOP, fill = tkinter.BOTH, expand = 1) 

menu_bar = tkinter.Menu(root) #create menu, passing in the root window
root.config(menu = menu_bar) #config root so that its menu is the menu created
model_menu = tkinter.Menu (menu_bar)
menu_bar.add_cascade (label = "Dodgems Model", menu = model_menu) #add menu as dropdown
model_menu.add_command (label = "Run model", command = run) #bind run func 
tkinter.mainloop()



# Outputting arena data as a json file
f = open ('out.json', 'w') #create json file called 'out', write mode
json.dump (arena, f) #dump 2D arena list data into the json file 'out'
f.close() #close json file



        

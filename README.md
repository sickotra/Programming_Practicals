# A Simple Agent Based Model Using Object Oriented Programming - Sept 2020

The model is a simulation where several agents interact with each other and the environment they are in by various behaviours such as move, eat and sharing resources.
A UML class diagram for the ABM program is included in the repository. 

# Table of Contents
1. [Repository Contents](#repo_contents)
2. [Running the Program](#running)
3. [Features](#features)
4. [Visualisations (Outputs)](#outputs)
5. [Potential Development](#develop)
6. [Sources](#sources)

## Repository Contents <a name="repo_contents"></a>
* *README.md*- This current read me file providing more information on the program
* *LICENSE* - GNU General Public License, version 3 (GPLv3)
* *model.py* - Main class to be run
* *agentframework.py* - Contains agents' behaviours class
* *in.txt* - initial environment data
* *out.json* - final environment data
* *UML_diagram.png* - Image of the UML class diagram
* *UML_diagram.xml* - XML format to allow editing

## Running the Program <a name="running"></a>
The number of agents, number of iterations of the random walks and the neighbourhood can be entered as arguments respectively from the anaconda command prompt/terminal by

`python  model.py  arg1 = 10  arg2 = 100  arg3 = 20`,

where the default arguments will be used if none are specified by the user. Only integer values should be used as arguements. 

Note: Code written using Python version 3.8.3 and so a version of Python 3 should be used to run the code.


## Features <a name="features"></a>
The agents are object instances from the `Agent` class in `agentframework.py`. All agent behaviours are defined in this class. The agents have coordinates from data downloaded from the web and any missing `y`, `x` values are set to be random integers between 0 and 99. The `y`, `x` variables have also been protected.

The agents interact with the environment and with themselves. The environment data, in which the agents exist, is read into the program from the CSV file `in.txt`. After running the program, the environment data is outputted as a JSON file `out.json`.

The agents have several behaviours. Each agent is given access to the environment and the locations of all other agents so they can communicate. The agents move, eat and share their resources with neighbouring agents. The movement is based on random walks and once they ‘eat’ the environment, it is added to their stores. The value of the neighbourhood can be chosen by the user. If the distance between two agents is less than the neighbourhood value, then the agents share resources from their stores. 


## Visualisations (Outputs) <a name="outputs"></a>
Once the file is run, 2 figures and a GUI called 'Model' will be outputted:
* Fig 1: A plot to visualise the agents locations and the environment they have eaten will be shown.
The maximum agents in the `y` and `x` direction will be overlaid in blue/red respectively with square markers. The maximum/minimum distance between the agents will be calculated. The search process is optimised so that it does not repeat pairs of agents or test agents against themselves. The time taken to do this is recorded. 
* GUI Model: This is a window with a dropdown menu that will allow the user to run the model again. This will run an animation (when window is full screen) and show the agents’ movement. The animation continues until a stopping condition has been reached and when there has been `num_of_iteration` iterations. 
* Fig 2: This figure will update once the animation is run through the GUI, the agents locations will be the same as Fig 1 to confirm the animation has run correctly.

## Potential Development <a name="develop"></a>

## Sources <a name="sources"></a>
GEOG5995M Programming for Social Science: Core Skills practicals (https://www.geog.leeds.ac.uk/courses/computing/study/core-python-phd/)

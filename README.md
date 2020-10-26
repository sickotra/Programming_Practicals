# Dodgy Dogems: Adapted ABM - Oct 2020
** Not finished yet **

# Table of Contents
1. [Repository Contents](#repo_contents)
2. [Further Development Idea](#idea)
3. [Variable Modifications](#mods)
4. [Running the Program](#running)


## Repository Contents <a name="repo_contents"></a>
* *README.md*- This current read me file providing more information on the program
* *LICENSE* - GNU General Public License, version 3 (GPLv3)
* *dodgem_model.py* - Main class to be run
* *dodgem_framework.py* - Contains dodgems' behaviours class
* *in.txt* - initial arena power data
* *out.json* - final arena power data

## Further Development Idea <a name="idea"></a>
The model is essentially the same but with the **added element of removing objects from a list**.

The model idea is to have 'faulty' dodgems/bumper cars (the agents) moving around the arena (the environment). The dodgems are faulty because they are old and the steering does not work and hence their movements are random and so they can be modelled using a random walk. 

The additional elements would be that the `Dodgem` class would have an extra `damage` attribute. When the dodgems bump into each other, the damage value of each increases and when the damage is significant the dodgem would stop moving. These dodgems would then be removed from the `dodgems` list and only working dodgems would remain. A new `collide` method in the `Dogems` class has been created to use for this. 

The dodgems are also faulty in regards to the power. When there are two cars near each other, they can have a boost in charge/electricity (similar to `share_with_neighbours` method). This boost is reflected by depleting power from the arena and adding to the two dodgem's `elec_store` class attribute. However, if the electricity store of the dodgem hits 0, the dodgem is out of power and should also be removed from the `dodgems` list. 


## Variable Modifications <a name="mods"></a>
Each dodgem is created using the `Dodgems` class with behaviours similar to the Agents model. 
Some of the variable names have been modified to add context:
* `Agents` class = `Dodgems` class
* `agents` list = `dodgems` list
* `environment` = `arena`
* `num_of_agents` = `num_of_dodgems`
* `eat` method = `power` method


## Running the Program <a name="running"></a>
The number of dodgems, number of iterations of the random walks and the neighbourhood can be entered as arguments respectively from the anaconda command prompt/terminal by

`python  model.py  arg1 = 10  arg2 = 100  arg3 = 20`,

where the default arguments will be used if none are specified by the user. Only integer values should be used as arguements. 

Note: Code written using Python version 3.8.3 and so a version of Python 3 should be used to run the code.


"""
    Main Driver Function
"""
import numpy as np
from Agentc.Agent import Agent
from Agentc.Location import Location 


names = ["kart", "zane", "nitamb", "leffy", "charter", "abe"]
mass = 15.0
locations = [
              [1,4.3, 5],
              [-1.3, 5.4, 1.2],
              [1,21,1],
              [123, 43,44],
              [1,-21,1],
              [-44,5,6]
        ]
agents = []
for i in names:
    agents.append( Agent(i, mass, np.random.randint(1,10), locations[names.index(i)]) )
    
for i in agents:
    print(i)
        
        
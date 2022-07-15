"""
 Author: Draken Wan
 
 
 3D Agent movement
 
 
"""
import Location as L

class Agent:
    tags = []
    
    def __init__(self, tag, mass, intel, location):
        """


        Parameters
        ----------
        tag : str
            it is an identification of an Agent
            it must be unique else error will return
            
        mass : float
            mass of the agent.
        intel : ranked int
            a ranked integer value within range 1-10.
        location : Location
            location of the agent

        Returns
        -------
        None.
        
        0utputs
        -------
         prints the name of the agent in the system and their location

        """
        assert type(tag) == str, "tag is an identification in string"
        assert tag not in Agent.tags, "tag must be unique. define again."
        assert type(mass) == float, "Mass must be a float"
        assert type(intel) == int, "intel must be a ranked integer"
        assert intel >= 0 and intel <= 10, "intel is a ranked integer 0-10"
        assert type(location) == list, "location must belong to class list"
        
        self.tag = tag
        Agent.tags.append(self.tag) # update the Agent names list for assertion to work
        self.mass = mass
        self.intel = intel
        self.loc = L.Location()
        self.move(location[0],location[1],location[2], False)
        
        print("Agent ", self.tag, " created at location ", self.loc)
    
    
    def update_mass(self, mass):
        
        assert type(mass) == float, "Mass should be a float"
        self.mass = mass
        
    def update_intel(self, intel):
        assert type(intel) == int, "intel must be a ranked integer"
        assert intel >= 0 and intel <= 10, "intel is a ranked integer 0-10"
        
        self.intel = intel
        
    def move(self, x, y, z, verbose=True):
    
        if verbose:
            print("Agent ",self.tag ," moved from " , self.loc, end="")
        
        self.loc.change_location(x, y, z, False)
        
        if verbose:
            print(" to " , self.loc)
    
        
    
class Location:
    def __init__(self, x=0., y=0., z=0.):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        
    def change_location(self, x=0., y=0., z=0., verbose=True):
        displacement = ( (self.x - x)**2 + (self.y - y)**2 + (self.z - z)**2 ) ** 0.5
        
        self.x = x
        self.y = y
        self.z = z
        
        if verbose:
            print("\ndisplacement: ", displacement)
    
    def __str__(self):
        _print = "("+str(self.x)+","+str(self.y)+","+str(self.z)+")"
        return _print
    

class Cordinate():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def sum(self,c1, c2):
        ss = c1 + c2
        return(ss)
    def dis(self,aa):
        x_diff = (self.x - aa.x)**2
        y_diff = (self.y - aa.y)**2
        z_diff = (self.z -aa.z)**2
        return((x_diff + y_diff + z_diff)**0.5)


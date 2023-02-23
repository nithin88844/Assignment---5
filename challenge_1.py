class point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqsum(self):
        return ((self.x)**2)+((self.y)**2)+((self.z)**2)
    
point_obj = point(int(input("Enter value of x : ")),int(input("Enter value of y : ")),int(input("Enter value of z : ")))
print(point_obj.sqsum())
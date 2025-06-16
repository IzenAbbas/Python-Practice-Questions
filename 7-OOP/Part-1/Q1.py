class Rectangle:
    def __init__(self,length=0,width=0):
        if(length==0 or width==0):
            raise ValueError('Invalid Parameters of Rectangle.')
        self.length=length
        self.width=width
    
    def Perimeter(self):
        return 2*self.length + 2*self.width
    
    def Area(self):
        return self.width*self.length
    
    def display(self):
        print('The Length of Rectangle is:', self.length)
        print('The Width of Rectangle is:', self.width)
        print('The Parameter of Rectangle is:', self.Perimeter())
        print('The Area of Rectangle is:', self.Area())
        
    
my_rectangle = Rectangle(3 , 4)
my_rectangle.display()
from abc import ABC,abstractmethod
class Polygon(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Polygon):
    def __init__(self,l,b):
        self.length=l
        self.width=b

    def area(self):
        return self.width*self.length


class Triangle(Polygon):
    def __init__(self, l, h):
        self.length = l
        self.height = h

    def area(self):
        return self.height * self.length*0.5

print('Area of rectangle:',Rectangle(4,5).area())
print('Area of triangle:',Triangle(4,5).area())
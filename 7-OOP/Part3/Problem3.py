class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __str__(self):
        return '({} , {})'.format(self.x,self.y)

class Location:
    def __init__(self,loc,des):
        self.location=loc
        self.destination=des

    def __str__(self):
        return 'Location: ({} , {})\nDestination: ({} , {})'.format(self.location.x,self.location.y,self.destination.x,self.destination.y)

    def reflection(self):
        print('Reflection of Location is: ({} , {})'.format(self.location.x,-self.location.y))



loc = Point(3, 5)
des = Point(7, 9)
place = Location(loc, des)
print(place)
place.reflection()

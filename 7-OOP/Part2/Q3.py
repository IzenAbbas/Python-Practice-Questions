class Rectangle:
    def __init__(self,l,h):
        self.__height=h
        self.__length=l

    def area(self):
        return self.__length*self.__height

    def is_square(self):
        return True if self.__height == self.__length else False

    def display(self):
        print('\n<<--Rectangle Details-->>')
        print('Length:',self.__length)
        print('Height:',self.__height)
        print('Area:',self.area())
        print('Is Square?',self.is_square())
        print('<<--------------------->>\n')


for i in range(1,10):
    for j in range(5,16):
        Rectangle(i,j).display()


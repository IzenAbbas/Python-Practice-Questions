class Scoop:
    total=0
    def __init__(self,f):
        self.flavor=f
        self.__price=None
        Scoop.total += 1
    @staticmethod
    def sold():
        print(f'{Scoop.total} Scoops sold')

    def set_price(self,p):
        self.__price=p
    def get_price(self):
        return self.__price

    def __str__(self):
        return 'Flavor - {} Price - {}'.format(self.flavor,self.__price)

class Bowl:
    total=0
    def __init__(self):
        self.__scoop_list=[]
        Bowl.total+=1

    @staticmethod
    def sold():
        print(f'{Bowl.total} Bowls sold')

    def add_scoops(self,*args):
        for i in args:
            self.__scoop_list.append(i)

    def __str__(self):
        s=''
        for i in self.__scoop_list:
            s+=i.flavor
            s+='\n'
        return s

    def display(self):
        price=0
        print ('Displaying Bowl')
        for i in self.__scoop_list:
            print(i)
            price+=i.get_price()
        print('Price of Bowl:',price)


choco = Scoop('chocolate')
print(choco)
choco.set_price(100)

berry = Scoop('berry')
berry.set_price(120)
print(berry)

vanilla = Scoop('vanilla')
vanilla.set_price(150)
bowl = Bowl()
bowl.add_scoops(choco) # Giving one parameter
bowl.add_scoops(berry, vanilla) # Multiple
# # add_scoops should handle both
#
print(bowl)
#
bowl.display()

Scoop.sold()
Bowl.sold()

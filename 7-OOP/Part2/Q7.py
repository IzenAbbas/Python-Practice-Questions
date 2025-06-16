class Scoop:
    total=0
    def __init__(self,f,n=1):
        self.flavor=f
        self.__price=None
        self.no_of_scoop=n
        Scoop.total += 1
    @staticmethod
    def sold():
        print(f'{Scoop.total} Scoops sold')

    def set_price(self,p):
        self.__price=p
    def get_price(self):
        return self.__price

    def __str__(self):
        return 'Flavor - {}, No of Scoops - {}, Price - {}'.format(self.flavor, self.no_of_scoop, self.__price)

class Bowl:

    total = 0
    def __init__(self, max_scoops=3):
        self.__max_scoops=max_scoops
        self.__scoop_list=[]
        Bowl.total+=1
        self.count=0

    @staticmethod
    def sold():
        print(f'{Bowl.total} Bowls sold')

    def add_scoops(self, *args):
        for i in args:
            if self.count + i.no_of_scoop <= self.__max_scoops:
                self.__scoop_list.append(i)
                self.count += i.no_of_scoop
                print(f'{i.flavor} added')
            else:
                if self.count == self.__max_scoops:
                    print('Bowl is full')
                else:
                    print(f'{i.flavor} not added. Bowl is full!!')

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
            price+=i.get_price()*i.no_of_scoop
        print('Price of Bowl:',price)


# Testing Code-1
choco = Scoop('chocolate', 1)
choco.set_price(100)
print(choco)


berry = Scoop('berry', 2)
berry.set_price(120)
print(berry)

vanilla = Scoop('vanilla') # no of scoop parameter not given, will take default value
vanilla.set_price(150)
print(vanilla)

# Testing Code-2
bowl1 = Bowl() # max_scoop parameter not given, will take default value
bowl1.add_scoops(choco) # Giving one parameter
bowl1.add_scoops(berry, vanilla) # Multiple
bowl1.display()

# Testing Code-3
bowl2 = Bowl(2)
bowl2.add_scoops(berry)
bowl2.add_scoops(choco)

bowl2.display()
Bowl.sold()



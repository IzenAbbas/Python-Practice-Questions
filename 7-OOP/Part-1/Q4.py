import random

class FlashCard():
    def __init__(self):
        self.__fruits={'Banana':'yellow','Strawberry':'pink','WaterMelon':'Green','Apple':'red'}
        print('Welcome to Fruit Quiz!')
        self.start_game()

    def generate_random(self):
        key=random.choice(list(self.__fruits.keys()))
        return key
    
    def is_guessed(self,key,guess):
        if(self.__fruits[key].lower()==guess.lower()):
            return True
        return False


    def start_game(self):
        selected=self.generate_random()
        guess=input('What is the color of {}: '.format(selected))
        if(self.is_guessed(selected,guess)):
            print('Correct Answer')
        else:
            print('Wrong Answer')

        again=input('Enter 0, if you want to play again: ')
        if(again=='0'):
            self.start_game()
        else:
            print('Game Exited!')
            exit()

f1=FlashCard()




        

    
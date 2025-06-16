import random


class Deck:
    __suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    __values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self):
        self.__deck=[Card(suit, value) for suit in Deck.__suits for value in Deck.__values]

    def deal(self):
        i=random.randrange(0, len(self.__deck))
        print(self.__deck[i], 'is removed')
        self.__deck.pop(i)
        random.shuffle(self.__deck)


    def print_deck(self):
        print('<<--DECK-->>')
        for i in self.__deck:
            print(i)
        print('<<-------->>')


class Card:

    def __init__(self,suit,value):
        self.suit=suit
        self.value=value

    def __str__(self):
        return "({}, {})".format(self.suit,self.value)


d1=Deck()
d1.print_deck()
d1.deal()
d1.print_deck()

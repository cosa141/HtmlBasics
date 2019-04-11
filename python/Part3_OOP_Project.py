from random import shuffle

suit = 'H D S C'.split()
rank = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    def __init__(self):
        self.cards=[(s,r) for s in suit for r in rank]
        print('Fresh Deck has been Created!')
    def __len__(self):
        return len(self.cards)
    def showDeck(self):
        return self.cards
    def shuffling(self):
        shuffle(self.cards)
    def splitHalf(self):
        return (self.cards[:26],self.cards[26:])

class Hand:
    def __init__(self,card):
        self.card=card
    def addCards(self,cardsToAdd):
        self.card.extend(cardsToAdd)
    def removeCard(self):
        return self.card.pop()
    def __str__(self):
        return len(self.card)
class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self,playerName):
        self.playerName=playerName
    def


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")
b=Deck()
print(b.showDeck())
print(len(b))


# Use the 3 classes along with some logic to play a game of war!

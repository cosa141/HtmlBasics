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
    def __init__(self,playerName,hand):
        self.playerName=playerName
        self.hand=hand
    def remainingCards(self):
        return len(self.hand.card)
    def playCard(self):
        drawnCard=self.hand.removeCard()
        print('{} has placed: {}'.format(self.playerName,drawnCard))
        print('\n')
        return drawnCard
    def war(self):
        warCards=[]
        if len(self.hand.card)<3:
            return warCards
        else:
            for x in range(3):
                warCards.append(self.hand.card.pop())
            return warCards
    def stillHasCards(self):
        return len(self.hand.card)!=0

######################
#### GAME PLAY #######
######################
total_rounds = 0
war_count = 0
print("Welcome to War, let's begin...")
b=Deck()
# print(b.showDeck())
# print(len(b))
b.shuffling()
han1,han2=b.splitHalf()
name=input('What is your name? ')
playa=Player(name,Hand(han1))
playb=Player('computer',Hand(han2))
# Use the 3 classes along with some logic to play a game of war!
while playa.stillHasCards() and playb.stillHasCards():
    total_rounds+=1
    print('Its time for a new round..')
    print('Here are the current standings: ')
    print(playa.playerName+' count: '+str(len(playa.hand.card)))
    print(playb.playerName+' count: '+str(len(playb.hand.card)))
    print("Both players play a card!")
    print('\n')
    table_cards = []
    a_card=playa.playCard()
    b_card=playb.playCard()
    table_cards.append(a_card)
    table_cards.append(b_card)
    if a_card[1]==b_card[1]:
        war_count+=1
        print('Its is war!!!!')
        table_cards.extend(playa.war())
        table_cards.extend(playb.war())
        a_card=playa.playCard()
        b_card=playb.playCard()
        if rank.index(a_card[1])<rank.index(b_card[1]):
            print(playa.playerName+' has the higher card, adding to hand!')
            playa.hand.addCards(table_cards)
        else:
            print(playb.playerName+' has the higher card, adding to hand!')
            playb.hand.addCards(table_cards)
    else:
        if rank.index(a_card[1])<rank.index(b_card[1]):
            print(playa.playerName+' has the higher card, adding to hand!')
            playa.hand.addCards(table_cards)
        else:
            print(playb.playerName+' has the higher card, adding to hand!')
            playb.hand.addCards(table_cards)
print('Great game, it lasted: '+str(total_rounds)+' rounds.')
print('A war occured '+str(war_count)+' times.')

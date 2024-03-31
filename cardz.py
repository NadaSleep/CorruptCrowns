import random

class Card:
    def __init__(self, suit, rank, name):
        self.suit = suit
        self.rank = rank
        self.name = name

class Deck:
    def __init__(self, suit, rank, name):
        self.suit = suit
        self.rank = rank
        self.name = name

    def Shuffle(self):
        random.shuffle(self.cards)
    
    def DrawReveal(self, amount):
        drawn = []
        for i in range(amount):
            drawn.append(self.cards.pop())
        return drawn

class CorruptCrowns:
    def __init__(self):
        self.corruptCrowns = 0
    
    def AddToDiscard(selfcard, discard):
        discard.append(Card)
        return discard
    
    def AddToBottomTavern(self,amount, tavern, Card):
        tavern.append(Card)
        return tavern

    def AddToHand(self,amount, hand, card):
        hand.append(Card)
        return hand

    def ShowHand(self,hand):
        return hand
    


if __name__ == "__main__":
   
  game = CorruptCrowns()

suitCastleDeckJ = ["S", "H", "D", "C"]
rankCastleDeckJ = ["J"]
castleDeckJ = game(suitCastleDeckJ, rankCastleDeckJ, "castleJ")

suitCastleDeckQ = ["S", "H", "D", "C"]
rankCastleDeckQ = ["Q"]
castleDeckQ = game(suitCastleDeckQ, rankCastleDeckQ, "castleQ")

suitCastleDeckK = ["S", "H", "D", "C"]
rankCastleDeckK = ["K"]
castleDeckK = game(suitCastleDeckK, rankCastleDeckK, "castleK")

suitTavernDeck = ["S", "H", "D", "C"]
rankTavernDeck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
tavernDeck = game(suitTavernDeck, rankTavernDeck, "tavern")

handDeck = []

discardDeck = []

castleDeck = castleDeckJ + castleDeckQ + castleDeckKs

tavernDeck = tavernDeck.shuffle()

handDeck = game.DrawReveal(8, tavernDeck)

print(handDeck)



  
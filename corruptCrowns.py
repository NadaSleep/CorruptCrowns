import random
# classes

# individual cards
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def suitPower(self,rank,suit):
        if rank.upper() == "A":
            rank = 1
        else:
           rank = int(rank)

        if self.suit == 'H':
            print("\nattack power: ", rank)

            if len(discard_deck.cards) == 0:
                print("\nNo cards in discard\n")
            else:
                # Shuffle the discard pile
                random.shuffle(discard_deck.cards)
                # Count out a number of cards facedown equal to the rank of active card           
                for i in range(rank):
                    card = discard_deck.cards.pop()
                    # Place the cards on bottom of the draw deck
                    draw_deck.cards.insert(0, card)
                pass
                   
        elif self.suit == 'D':        
          print("\nattack power: ", rank)
          while len(hand_deck.cards) < HANDLIMIT:
            card = draw_deck.draw()
            if card:
                hand_deck.cards.append(card)
            else:
                break    
            pass


        elif self.suit == 'C':
            attackPower = int(rank) * 2
            print("\nattack power: ", attackPower)        
            pass



        elif self.suit == 'S':
          print("\nattack power: ", rank)
          defense = 0
          defense += int(rank)
          print("Defense:", defense)

      
# deck of cards
class Deck:
    def __init__(self, ranks, suits):
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]

# draw card from deck
    def draw(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()
 
 # draw up to hand limit
    def drawHandLimit(self, hand_deck, limit):
        for i in range(limit):
            card = self.draw()
            if card is not None:
                hand_deck.cards.append(card)
            else:
                break

# play card from hand
    def playCard(self, playRank, playSuit):
        playSuit = playSuit.upper()
        for card in hand_deck.cards:
            if card.rank == playRank and card.suit == playSuit:
              hand_deck.cards.remove(card)
              return card
        return None

    def shuffle(self):
       random.shuffle(self.cards)


    def showHand(self):
        for card in self.cards:
          print(card.rank, card.suit)


HANDLIMIT = 8

# suits
suits = ['S', 'H', 'D', 'C']

# Castle Deck Jacks
castleDeck1 = ["J"]
jacks_deck = Deck(castleDeck1, suits)

# Castle Deck Queens
castleDeck2 = ["Q"]
queens_deck = Deck(castleDeck2, suits)

# Castle Deck Kings
castleDeck3 = ["K"]
kings_deck = Deck(castleDeck3, suits)

# Draw deck
draw_ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10']
draw_deck = Deck(draw_ranks, suits)

# Discard deck 
discard_deck = Deck([], [])

# Hand of cards
hand_deck = Deck([], [])

activeEnemyCard = jacks_deck.draw()
print("\nActive Enemy Card:\n", activeEnemyCard.rank, activeEnemyCard.suit)

print("")
print("\t\t\tHearts: Heal, add cards to bottom of draw from discard equal to rank played.")
print("\t\t\tDiamonds: Draw, draw cards from draw deck equal to rank played.")
print("\t\t\tClubs: Attack, double damage to enemy.")
print("\t\t\tSpades: Defend, reduce damage by rank played. Stacks against same enemy.")
print("\t\t\t")

# Method that shuffles the draw deck
draw_deck.shuffle()

# Drawing up to hand limit. Maybe change in a method to start game.
draw_deck.drawHandLimit(hand_deck, HANDLIMIT)
# Display hand of cards
print("\nCards in hand:")
hand_deck.showHand()

#play card from hand
playRank = input("\nEnter the rank of the card to play: ")
playSuit = input("\nEnter the suit of the card to play: ").upper()
 
activePlayerCard = Card(playRank, playSuit)

hand_deck.playCard(activePlayerCard.rank, activePlayerCard.suit)

hand_deck.showHand

print("\nActive Player Card:", activePlayerCard.rank, activePlayerCard.suit)



activePlayerCard.suitPower(activePlayerCard.rank, activePlayerCard.suit)    

print("\nCards in hand:")
hand_deck.showHand()





#classes
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    # def suitPower(self):
        

#deck of cards    
class Deck:
    def __init__(self, ranks, suits):
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]

#draw card from deck
    def draw(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()
 
 #draw up to hand limit  
    def drawHandLimit(self, hand_deck, limit):
        for i in range(limit):
            card = self.draw()
            if card is not None:
                hand_deck.cards.append(card)
            else:
                break

#play card from hand
    def playCard(self, playRank, playSuit):
        for card in hand_deck.cards:
            if card.rank == playRank and card.suit == playSuit:
              hand_deck.cards.remove(card)
              return card
        return None

HANDLIMIT = 8

# Castle Deck Jacks
castleDeck1 = ["J"]
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
jacks_deck = Deck(castleDeck1, suits)

# Castle Deck Queens
castleDeck2 = ["Q"]
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
queens_deck = Deck(castleDeck2, suits)

# Castle Deck Kings
castleDeck3 = ["K"]
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
kings_deck = Deck(castleDeck3, suits)

# Draw deck
draw_ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10']
draw_deck = Deck(draw_ranks, suits)

# Discard deck 
discard_deck = Deck([], [])

# Hand of cards
hand_deck = Deck([], [])

activeEnemyCard = kings_deck.draw()
print("Active Enemy Card:\n", activeEnemyCard.rank, activeEnemyCard.suit)

print("")
print("\t\t\tHearts: Heal, add cards to bottom of draw from discard equal to rank played.")
print("\t\t\tDiamonds: Draw, draw cards from draw deck equal to rank played.")
print("\t\t\tClubs: Attack, double damage to enemy.")
print("\t\t\tSpades: Defend, reduce damage by rank played. Stacks against same enemy.")
print("\t\t\t")
# Drawing up to hand limit. Maybe change in a method to start game.
draw_deck.drawHandLimit(hand_deck, HANDLIMIT)
print("HAND:")
for card in hand_deck.cards:
    print(card.rank, card.suit)

#play card from hand
playRank = input("\nEnter the rank of the card to play: ")
playSuit = input ("\nEnter the suit of the card to play: ")
 

activePlayerCard = hand_deck.playCard(playRank, playSuit)
print("\nActive Player Card:", activePlayerCard.rank, activePlayerCard.suit)



#classes
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
class Deck:
    def __init__(self, ranks, suits):
        self.cards = [Card(rank, suit) for rank in ranks for suit in suits]

    def draw(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop()
   
    def drawHandLimit(self, hand_deck, limit):
        for i in range(limit):
            card = self.draw()
            if card is not None:
                hand_deck.cards.append(card)
            else:
                break

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

# activeCastleCard = kings_deck.draw()
# print(activeCastleCard.rank, activeCastleCard.suit)

# Drawing up to hand limit. Maybe change in a method to start game.
draw_deck.drawHandLimit(hand_deck, HANDLIMIT)
print("HAND:")
for card in hand_deck.cards:
    print(card.rank, card.suit)
import random
# classes

# individual cards
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
# class to special effect of card determined by suit
    def suitPower(self,rank,suit):
# makes sure that the ace will have a value of 1 and also converts the rank to an integer
        if rank.upper() == "A":
            rank = 1
        else:
           rank = int(rank)
# if the suit is hearts, the player will heal by adding cards to the bottom of the draw deck       
        if self.suit == 'H':            
# displays the attack power of the card
            attackPower = int(rank)
            print("\nattack power: ", attackPower)
# check to see if the discard deck is empty
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
# if the suit is diamonds, the player will draw cards from the draw deck to hand                   
        elif self.suit == 'D':        
          attackPower = int(rank)
          print("\nattack power: ", attackPower)
          while len(hand_deck.cards) < HANDLIMIT:
            card = draw_deck.draw()
            if card:
                hand_deck.cards.append(card)
            else:
                break    
            pass
# if the suit is clubs, the player will attack the enemy with double the damage of the rank of the card
        elif self.suit == 'C':
            attackPower = int(rank) * 2
            print("\nattack power: ", attackPower)        
            pass
# if the suit is spades, the player will defend against the enemy with the rank of the card
        elif self.suit == 'S':
          attackPower = int(rank)
          print("\nattack power: ", attackPower)
          defense = 0
          defense += int(rank)
          print("Defense:", defense)

#   def checkDamage(self, activePlayerCard, activeEnemyCard):

# class JEnemyCard:
#     def __init__(self, suit, health = 20, attack = 10):
#         self.suit = suit
#         self.health = health
#         self.attack = attack    

# class QEnemyCard:
#     def __init__(self, suit, health = 30, attack = 15):
       
#         self.suit = suit
#         self.health = health
#         self.attack = attack

# class KEnemyCard:
#     def __init__(self, suit, health = 40, attack = 20):
#         self.suit = suit
#         self.health = health
#         self.damage = attack

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

# shuffle deck    
    def shuffle(self):
       random.shuffle(self.cards)


    def showHand(self):
        for card in self.cards:
          print(card.rank, card.suit)


# Health bar
class Player:
   def __init__(self, name, max_health):
       self.name = name
       self.max_health = max_health
       self.health = max_health

# Take damage
   def take_damage(self, damage):
       self.health -= damage
       if self.health < 0:
           self.health = 0

# Heal
   def heal(self, amount):
       self.health += amount
       if self.health > self.max_health:
           self.health = self.max_health

# Check if player is alive
   def is_alive(self):
       return self.health > 0

# Print health bar
   def print_health_bar(self):
       bar_length = 20
       filled_length = int(round(bar_length * self.health / self.max_health))
       bar = '█' * filled_length + '-' * (bar_length - filled_length)
       print(f'{self.name}\'s Health: [{bar}] {self.health}/{self.max_health}')

# Constant to set hand limit
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

# Initialize players
player = Player("Player", 20)
enemy = Player("Enemy", 20)

# Print updated health
player.print_health_bar()
enemy.print_health_bar()

# Draw active enemy card
activeEnemyCard = jacks_deck.draw()

print("\nActive Enemy Card:\n", activeEnemyCard.rank, activeEnemyCard.suit)

# Cheat sheet for the suit effects
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

#Play card from hand
playRank = input("\nEnter the rank of the card to play: ")
playSuit = input("\nEnter the suit of the card to play: ").upper()
 # Initialize active player card
activePlayerCard = Card(playRank, playSuit)
# play card
hand_deck.playCard(activePlayerCard.rank, activePlayerCard.suit)
# Display hand of cards
hand_deck.showHand
# Print active player card
print("\nActive Player Card:", activePlayerCard.rank, activePlayerCard.suit)
# Suit power
activePlayerCard.suitPower(activePlayerCard.rank, activePlayerCard.suit)    
# Show active enemy card
print("\nActive Enemy Card:\n", activeEnemyCard.rank, activeEnemyCard.suit)

# Print updated health
player.print_health_bar()
enemy.print_health_bar()
# Show cards in hand
print("\nCards in hand:")
hand_deck.showHand()




import random

class CastleDeck
    def__init__(self,rank,suit):
    self.rank = rank
    self.suit = suit

suitCd1 = ["S","H","D","C"]
rankCd1 = ["J"]

castleDeck1 = []
for suitCd1 in suitCd1:
    for rankCd1 in rankCd1:
        castleDeck1.append((rankCd1,suitCd1))

random.shuffle(castleDeck1)

topCard = castleDeck1.pop(0)
print(f"{topCard[0]}{topCard[1]}")

suitCd2 = ["S","H","D","C"]
rankCd2 = ["Q"]

castleDeck2 = []
for suitCd2 in suitCd2:
    for rankCd2 in rankCd2:
        castleDeck2.append((rankCd2,suitCd2))

random.shuffle(castleDeck2)

topCard2 = castleDeck2.pop(0)
print(f"{topCard2[0]}{topCard2[1]}")

suitCd3 = ["S","H","D","C"]
rankCd3 = ["K"]

castleDeck3 = []
for suitCd3 in suitCd3:
    for rankCd3 in rankCd3:
        castleDeck3.append((rankCd3,suitCd3))

random.shuffle(castleDeck3)

topCard3 = castleDeck3.pop(0)
print(f"{topCard3[0]}{topCard3[1]}")


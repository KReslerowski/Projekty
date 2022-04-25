import random

cardList = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen",
            "King", "King", "King", "King",
            "Ace", "Ace", "Ace", "Ace",
            "Joker", "Joker"]

random.shuffle(cardList)

print(cardList)

reka_1 = []

for i in range(0,5):
    reka_1.append(cardList.pop())
    
#print(cardList)

reka_2 = []

for i in range(0,5):
    reka_2.append(cardList.pop())
    
print(cardList)
print(reka_1)
print(reka_2)
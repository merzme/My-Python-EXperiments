
import random
t = ["stone","paper","scissors"]
comp = t[random.randint(0,2)]
player = False
while player == False:
     player = input("stone,paper,scissors:")
if player == comp:
    print("tie")
elif player == stone:

    if comp == paper:
        print("you lose" ,comp,"covers",player)
    else:
        print("you won ",player,"covers",comp)

elif player == paper:

    if comp == scissors:
        print("you lose",comp,"covers",player)
    else:
        print("you won ",player,"covers",comp)

elif player == scissors:
    if comp == stone:
        print("you lose",comp,"covers",player)
    else:
        print("you won ",player,"covers",comp)
else:
    print("That's not a valid play. Check your spelling!")

player = False
computer = t[random.randint(0,2)]

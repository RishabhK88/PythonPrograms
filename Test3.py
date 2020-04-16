# CodeWithHarry
# Exercise 6
# Snake Water Gun Game

import random
i = 0
compwin = 0
youwin = 0
tie = 0
while(i < 10):
    print("SNAKE WATER GUN GAME")
    list = ["Snake", "Water", "Gun"]
    compchoice = random.choice(list)
    print("Snake->s")
    print("Water->w")
    print("Gun->g")
    ch = input("Enter your choice(s/w/g): ")
    print(f"Computer's choice {compchoice}")
    print("\n")
    if(compchoice == "Snake" and ch == "s"):
        tie += 1
    elif(compchoice == "Snake" and ch == "w"):
        compwin += 1
    elif(compchoice == "Snake" and ch == "g"):
        youwin += 1
    elif(compchoice == "Water" and ch == "s"):
        youwin += 1
    elif(compchoice == "Water" and ch == "w"):
        tie += 1
    elif(compchoice == "Water" and ch == "g"):
        compwin += 1
    elif(compchoice == "Gun" and ch == "s"):
        compwin += 1
    elif(compchoice == "Gun" and ch == "w"):
        youwin += 1
    elif(compchoice == "Gun" and ch == "g"):
        tie += 1
    i += 1
if(compwin > youwin):
    print("Games Won")
    print(f"Computer: {compwin}")
    print(f"You: {youwin}")
    print(f"Ties: {tie}")
    print("Computer wins")
elif(youwin > compwin):
    print("Games Won")
    print(f"Computer: {compwin}")
    print(f"You: {youwin}")
    print(f"Ties: {tie}")
    print("You win")
elif(youwin == compwin):
    print("Games Won")
    print(f"Computer: {compwin}")
    print(f"You: {youwin}")
    print(f"Ties: {tie}")
    print("Nobody wins")
print("\n")

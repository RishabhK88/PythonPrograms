n = 8
i = 0
while(i < 9):
    guess = int(input("Guess the Number: "))
    if i >= 8:
        print("Game over")
        break
    elif guess > n:
        print("Go lower!")
    elif guess < n:
        print("Go higher!")
    elif guess == n:
        print("You win")
        break
    i += 1

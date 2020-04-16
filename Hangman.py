import random

print("HANGMAN")
Secretlist = ["awkward", "bagpipes", "banjo", "bungler", "croquet", "crypt", "dwarves", "fervid", "fishhook", "fjord", "gazebo", "gypsy", "haiku", "haphazard", "hyphen", "ivory", "jazzy", "jiffy", "jinx", "jukebox", "kayak", "kiosk", "klutz", "memento",
              "mystify", "numbskull", "ostracize", "oxygen", "pajama", "phlegm", "pixel", "polka", "quad", "quip", "rhythmic", "rogue", "sphinx", "squawk", "swivel", "toady", "welfth", "unzip", "waxy", "wildebeest", "yacht", "zealous", "zigzag", "zippy", "zombie"]

Secretword = Secretlist[random.randint(0, 49)]
print(Secretword)
i = 0
j = 0
k = 0
x = 0
while(i < len(Secretword)):
    print("-", end=" ")
    i += 1
for j in range(len(Secretword)):
    letter = input("\nGuess the letter: ")
    for k in range(len(Secretword)):
        if letter == Secretword[k]:
            while(x < len(Secretword)):
                if x == k:
                    print(letter)
                else:
                    print("-", end=" ")
                    x += 1

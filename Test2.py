# CodeWithHarry
# Exercise 5


def getdate():
    import datetime
    return datetime.datetime.now()


def FoodExerciseFile():
    print("File Option:")
    print("1. Food\n2. Exercise")
    global ch2
    ch2 = int(input("Enter your choice: "))


f = open("HarryFood.txt", "w")
f.write("Harry's Food\n")
f.close()
f = open("HarryExercise.txt", "w")
f.write("Harry's Exercise\n")
f.close()
f = open("RohanFood.txt", "w")
f.write("Rohan's Food\n")
f.close()
f = open("RohanExercise.txt", "w")
f.write("Rohan's Exercise\n")
f.close()
f = open("HammadFood.txt", "w")
f.write("Hammad's Food\n")
f.close()
f = open("HammadExercise.txt", "w")
f.write("Hammad's Exercise\n")
f.close()
ch3 = "y"
while(ch3 == "y" or ch3 == "Y"):
    print("HEALTH MANAGEMENT SYSTEM")
    print("1. Harry\n2. Rohan\n3. Hammad")
    ch1 = int(input("Enter your choice(1-3): "))
    if(ch1 == 1):
        FoodExerciseFile()
        if(ch2 == 1):
            f = open("HarryFood.txt", "a")
            food = input("Enter the food: ")
            f.write(str(getdate()))
            f.write(" ")
            f.write(food)
            f.close()
        if(ch2 == 2):
            f = open("HarryExercise.txt", "a")
            exercise = input("Enter the exercise: ")
            f.write(str(getdate()))
            f.write(" ")
            f.write(exercise)
            f.close()
    if(ch1 == 2):
        FoodExerciseFile()
        if(ch2 == 1):
            f = open("RohanFood.txt", "a")
            food = input("Enter the food: ")
            f.write(str(getdate()))
            f.write(" ")
            f.write(food)
            f.close()
        if(ch2 == 2):
            f = open("RohanExercise.txt", "a")
            exercise = input("Enter the exercise: ")
            f.write(str(getdate()))
            f.write(" ")
            f.write(exercise)
            f.close()
    if(ch1 == 3):
        FoodExerciseFile()
        if(ch2 == 1):
            f = open("HammadFood.txt", "a")
            food = input("Enter the food: ")
            f.write(str(getdate()))
            f.write(" ")
            f.write(food)
            f.close()
        if(ch2 == 2):
            f = open("HammadExercise.txt", "a")
            exercise = input("Enter the exercise: ")
            f.write(str(getdate()))
            f.write(" ")
            f.write(exercise)
            f.close()
    ch4 = input("Do you want to retrieve data?")
    if(ch4 == "y" or ch4 == "Y"):
        print("1. Harry\n2. Rohan\n3. Hammad")
        ch1 = int(input("Enter your choice(1-3): "))
        if(ch1 == 1):
            FoodExerciseFile()
            if(ch2 == 1):
                f = open("HarryFood.txt", "r")
                hfood = f.read()
                print(hfood)
                f.close()
            if(ch2 == 2):
                f = open("HarryExercise.txt", "r")
                hexercise = f.read()
                print(hexercise)
                f.close()
        if(ch1 == 2):
            FoodExerciseFile()
            if(ch2 == 1):
                f = open("RohanFood.txt", "r")
                rfood = f.read()
                print(rfood)
                f.close()
            if(ch2 == 2):
                f = open("RohanExercise.txt", "r")
                rexercise = f.read()
                print(rexercise)
                f.close()
        if(ch1 == 3):
            FoodExerciseFile()
            if(ch2 == 1):
                f = open("HammadFood.txt", "r")
                hafood = f.read()
                print(hafood)
                f.close()
            if(ch2 == 2):
                f = open("HammadExercise.txt", "r")
                haexercise = f.read()
                print(haexercise)
                f.close()
    if(ch4 == "n" or ch4 == "N"):
        exit
    ch3 = input("Do you want to continue(y/n)")
    if(ch3 == "n" or ch3 == "N"):
        exit

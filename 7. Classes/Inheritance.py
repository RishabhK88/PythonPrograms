# We can see that eat function is common in both classs. Repition is not a good
# practice in programming. So we will use inheritance so second class will inherit
# from first class


class Mammal:
    def eat(self):
        print("eat")

    def walk(self):
        print("walk")


class Fish:
    def eat(self):
        print("eat")

    def swim(self):
        print("swim")


class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal1(Animal):
    def walk(self):
        print("walk")


class Fish1(Animal):
    def swim(self):
        print("swim")


m = Mammal1()
m.eat()
print(m.age)

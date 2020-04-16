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
# It checks if an object is instance of given class
print(isinstance(m, Animal))
print(isinstance(m, Mammal1))
# All classes in python are inherited from a class called object
print(isinstance(m, object))
# Is subclass checks if a class is derived from the other class or not
print(issubclass(Mammal1, Animal))

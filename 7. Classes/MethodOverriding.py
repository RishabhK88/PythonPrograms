class Animal:
    def __init__(self):
        self.age = 1
        print("Animal Constructor")

    def eat(self):
        print("eat")


class Mammal1(Animal):

    def __init__(self):
        super().__init__()  # To avoid method overriding. In this case constructor of
        # animal was called first and then of mammal, but if we place this
        # statement below self.weight=2, constructor of mammal will be called
        # first and then of animal
        print("Mammal Constructor")
        self.weight = 2

    def walk(self):
        print("walk")


class Fish1(Animal):
    def swim(self):
        print("swim")


m = Mammal1()
print(m.age)
print(m.weight)

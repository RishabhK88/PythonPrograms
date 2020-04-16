class Point:
    def __init__(self, x, y):    # Magic Methods are methods with 2 underscores
        # initially. They are called by python interpreter and dont need to be called
        # List of magic methods can be found in python documentation
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
point.draw()
print(str(point))

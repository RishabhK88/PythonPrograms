# self is a reference to current point object
class Point:
    def __init__(self, x, y):    # Constructor
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
print(point.x)
print(point.y)
point.draw()

class Point:
    def __init__(self, x, y):    # Constructor
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):  # Class Method
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point.zero()  # Class Method
point.draw()  # Instance Method

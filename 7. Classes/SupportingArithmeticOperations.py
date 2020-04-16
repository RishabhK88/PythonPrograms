# We also have magic methods for performing arithmetic operations between objects
class Point:
    def __init__(self, x, y):    # Constructor
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)


point = Point(1, 2)
other = Point(1, 2)
combined = point + other
print(combined.x)
print(combined.y)

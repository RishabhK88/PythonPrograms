# Class is a blue print for creating new objects
# Object are instance of a class


class Point:
    def draw(self):
        print("Draw")


point = Point()
print(type(point))
print(isinstance(point, Point))

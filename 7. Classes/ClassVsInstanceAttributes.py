class Point:
    default_color = "red"  # Class level attribute. We can read this via class
    # reference(line 19) or object referance(line 18)

    def __init__(self, x, y):    # Constructor
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
point.z = 10  # We can define attributes later also, it is not necessary to declare
# all of them in constructor. The above attribute is specific to instance point.
# Class attributes are declared in class are shared accross all instances of a class.
point.draw()
print(point.default_color)
print(Point.default_color)

another = Point(3, 4)
another.draw()

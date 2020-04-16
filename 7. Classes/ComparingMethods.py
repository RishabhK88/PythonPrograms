class Point:
    def __init__(self, x, y):    # Constructor
        self.x = x
        self.y = y


point = Point(1, 2)
other = Point(1, 2)
print(point == other)
# In the above statement we get false because by default the == operator compares
# the memory address of the 2 objects and they are stored at different memory
# locations, even though what they contain is same. So, in this case we use magic
# methods.


class Point1:
    def __init__(self, x, y):    # Constructor
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


point = Point1(1, 2)
other = Point1(1, 2)
print(point == other)
# Here we get true because we used magic methods. Similarly > or < operators are not
# supported in case of comparing instances. So, we have to use another magic method
# These magic methods can be found in python documentation.

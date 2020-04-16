# Tuple is a read only list. We cannot  modify it
point = (1, 2)
# If we don't use paranthesis, python takes it to be a tuple
point = 1, 2
print(type(point))
# Empty paranthesis can be made by using empty paranthesis
# We can concatenate a tuple
point = (1, 2) + (3, 4)
print(point)
# We can also repeat a tuple
point = (1, 2) * 3
print(point)
# We can also convert list to tuple usind tuple function
point = tuple("Hello World")
print(point)
point = tuple([1, 2, 3])
print(point)
# We can access individual items using index
print(point[1])
print(point[0:2])
# Above operations are exactly like lists
# We can unpack a tuple
x, y, z = point
# Tuples are also iterable

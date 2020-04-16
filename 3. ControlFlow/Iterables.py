print(type(5))
print(type(range(5)))
# since range() is used in loops it is iterable
# similarly strings can also be iterable in python
for char in "Python":
    print(char)
# each char will store a character of the string

# lists are also iterables
for x in [1, 2, 3, 4]:
    print(x)
# each x stores an element of list

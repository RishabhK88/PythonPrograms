from sys import getsizeof

values = [x*2 for x in range(10)]
for x in values:
    print(x)

# If there is a large number of data or infinite stream of data, we should not store
# it in memory since it is very memory inefficient. In situations like this it is
# more efficient to use generator object. They are iterable and in each iteration
# they generate a new value instead of storing them in memory. This can be done by
# replacing square brackets by paranthesis in line 1

values = (x*2 for x in range(10))
print(values)
for x in values:
    print(x)

# Generator object takes very less space in memory.
# To check this we can import getsizeof from sys which is used to tell size of
# object
values = (x*2 for x in range(1000))
print("Generator1:", getsizeof(values))
values = (x*2 for x in range(1000000))
print("Generator2:", getsizeof(values))
# The size of generator object remains constant in both above cases unlike if we use
# lists
values = [x*2 for x in range(1000)]
print("List1:", getsizeof(values))
values = [x*2 for x in range(1000000)]
print("List2:", getsizeof(values))

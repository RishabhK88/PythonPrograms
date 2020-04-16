numbers = [1, 2, 3]
print(numbers)
# To unpack the operator we can use * symbol
print(*numbers)
# Unpacking operator can be used with any iterable
values = [*range(5), *"Hello"]
print(values)
# We can also use it to combine strings
combined = [*numbers, *values]
print(combined)

# We can also unpack dictionaries by using ** signs follows
first = dict(x=1)
second = dict(x=10, y=20)
combined = {**first, **second}
print(combined)

# If we have multiple values, combined dictionary will take the last value

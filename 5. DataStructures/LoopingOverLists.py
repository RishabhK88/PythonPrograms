letters = ["a", "b", "c"]
for letter in letters:
    print(letter)
# enumerate() is used to create tuples of numbers and elements of list
for letter in enumerate(letters):
    print(letter)
for index, letter in enumerate(letters):
    print(f"{index}: {letter}")
# We can also unpack a tuple

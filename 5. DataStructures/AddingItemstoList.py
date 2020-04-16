letters = ["a", "b", "c"]
# To add elements at the end of the list we use the append method
letters.append("d")
print(letters)
# To add elements at a specific position in the list we insert
letters.insert(0, "#")
print(letters)
# To remove item from end of list
letters.pop()
print(letters)
# To remove item at given index
letters.pop(1)
print(letters)
# To remove known element
letters.remove("#")
print(letters)
# delete statement
numbers = list(range(8))
print(numbers)
del numbers[0]
print(numbers)
del numbers[0:3]
print(numbers)
# The delete statement can also delete range of objects of list as above
letters.clear()
print(letters)
# Use clear to delete all elements of list

# Set is also a data structure which is collection with no duplicates
# So say we have list of numbers with duplicates. We can convert it into set to remove
# duplicates
numbers = [1, 2, 2, 2, 3, 4, 4]
uniques = set(numbers)
print(uniques)
# Curly braces used to define sets
set1 = {1, 2, 3, 4}
# We can operate on sets that is use append(), remove() etc. on sets same as we do
# on lists
# We can also use len() to find number of elements in set
# Sets are unique because of the powerful mathematical operations that can be
# performed on sets
set2 = {4, 5, 6, 7}
# Union operation is denoted by |
union = set1 | set2
print(union)
# Intersection is denoted by &
intersection = set1 & set2
print(intersection)
# Difference is denoted by -
difference = set1 - set2
print(difference)
# Symmetric difference retuens items that are either in forst or second set but not
# both. It is denoted by ^
sym_diff = set1 ^ set2
print(sym_diff)

# Sets are unordered lists, they dont have a sequence, so we cannot access them
# using an index
# Instead we can check existence of an element in a set

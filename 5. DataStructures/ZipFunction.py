list1 = [1, 2, 3]
list2 = [10, 20, 20]
# If we want to convert the above 2 lists to -> [(1, 10), (2, 20), (3, 30)] we use
# zip function
print(list(zip(list1, list2)))
# Zip function gives a list object which is iterable and can also be converted to
# list.
# Zip function can also take strings as parameters as strings are also iterables
# You can zip 2 or more iterables together

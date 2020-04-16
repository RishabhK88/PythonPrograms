items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)


]
# To filter the list(say for example finding items with price more than 10),
# we can iterate over the list, but it is a tedious process
# so we used filter function

x = filter(lambda item: item[1] >= 10, items)
print(x)
# Above gives a filter object which is iterable
for item in x:
    print(item)
# It can also be converted into list
y = list(filter(lambda item: item[1] >= 10, items))
print(y)

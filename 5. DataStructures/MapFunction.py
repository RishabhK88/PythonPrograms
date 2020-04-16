# Map function is used to get a new list of elements from original list
items = [
    ("Product1", "10"),
    ("Product2", "9"),
    ("Product3", "12")

]
prices = []
for item in items:
    prices.append(item[1])

print(prices)
# The above can also be done elegantly with map function as follows

x = map(lambda item: item[1], items)
print(x)
# The above code gives a map object which is iterable
for item in x:
    print(item)
# Furthermore we can convert map object into list
prices = list(map(lambda item: item[1], items))
print(prices)

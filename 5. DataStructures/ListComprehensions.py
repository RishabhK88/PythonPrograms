items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)

]

prices = list(map(lambda item: item[1], items))
# The above code can also be written as(list comprehension)
prices = [item[1] for item in items]

filtered = list(filter(lambda item: item[1] >= 10, items))
# The above code can also be written as(list comprehension)
filtered = [item[1] >= 10 for item in items]

print(prices)
print(filtered)

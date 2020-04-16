# Lambda is a one line anonymous function that we can pass to other functions

# To sort something like a bunch of tuples such as in items below, we have to define
# a function
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)

]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)
# The above code of the function is very time consuming and so the above can also be
# done using lambda function

items.sort(key=lambda item: item[1])
print(items)
# syntax of lambda function is key=lambda parameters:expression

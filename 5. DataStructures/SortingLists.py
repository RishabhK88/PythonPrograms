numbers = [3, 51, 2, 8, 6]
# List is sorted in ascending order
numbers.sort()
print(numbers)
# List is sorted in descending order
numbers.sort(reverse=True)
print(numbers)
# Below is used to sort the list and print but not change the original list
print(sorted(numbers))
print(sorted(numbers, reverse=True))
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

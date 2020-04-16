# the below code accepts a many arguments in the form of tuple, which are like
# lists but cannot be edited. they are also iterable
# * sign is used to accept a collection of arguments in form of tuple


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

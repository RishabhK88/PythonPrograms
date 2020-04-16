# Unpacking lists means getting elements of list individeually into multiple variables
numbers = [1, 2, 3]
first, second, third = numbers
print(first)
print(second)
print(third)
# The above line of code is same as
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]
# While unpacking the number of variables specified should be equal to number of
# elements on list
number2 = list(range(8))
print(number2)
# if we want to unpack for example only first 3 variables, we can unpack 3 and pack
# the others in another list as follows
fir, sec, thir, *other = number2
# the above code unpacks first 3 variables and pack the rest in a list called other
print(other)
print(fir)
print(sec)
print(thir)
# if we only want to unpack first and last variable
fir, *other, last = number2
print(fir)
print(last)
print(other)

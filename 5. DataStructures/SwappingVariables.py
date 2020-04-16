x = 10
y = 11
print(f"{x}, {y}")
temp = x
x = y
y = temp
print(f"{x}, {y}")
# The above swapping can be done very easily in python using following line of code
x, y = y, x
# Explanation of above line
# There are tuples on both side of equality sign. The tuples are unpacked and
# variables are assigned, which leads to swapping
# It is same as
# a, b = 1, 2 which assigns 1 to a and 2 to b

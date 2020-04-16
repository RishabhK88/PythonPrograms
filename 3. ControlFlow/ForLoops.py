# The below code explains loops
# it is self explanatory

for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

# for ranges
for number in range(1, 4):
    print("Attempt", number + 1, (number + 1) * ".")

# for steps: first parameter is initial value of range, second parameter is the
# last value of range and third parameter is the number of steps to be skipped
# below is an example
for number in range(1, 10, 2):
    print("Attempt", number + 1, (number + 1) * ".")
# so output will be 2, 4, 6, 8, 10 i.e. at differnce of 2

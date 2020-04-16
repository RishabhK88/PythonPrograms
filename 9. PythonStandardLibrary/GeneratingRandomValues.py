import random
import string
print(random.random())  # random float value
print(random.randint(1, 10))  # random integer between 2 numbers
print(random.choice([1, 2, 3, 4]))  # Picks random object in array

# Picks k nimber of random objects in array
print(random.choices([1, 2, 3, 4], k=2))

print("".join(random.choices("abcdefghij", k=4)))
print(string.ascii_letters)

print("".join(random.choices(string.ascii_letters+string.digits, k=4)))


numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)

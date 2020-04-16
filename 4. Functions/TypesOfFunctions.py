# 2 types of functions:
# one performs a task
# the other returns a values
# 1st type


def greet(name):
    print(f"Hi, {name}")
# 2nd type


def get_greeting(name):
    return f"Hi, {name}"


message = get_greeting("Rishabh")
print(message)

print(greet(None))
# the above function will return None since it does not return a value
# printing a function basically prints its return value

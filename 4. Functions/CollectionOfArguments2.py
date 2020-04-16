# like before * is used to accept arguments in form of tuple, similarly, ** is used
# to accept arguments in form a dictionary(which contains key value pairs in which
# values can be accesed by calling keys as shown below). dictionaries is a complex data
# type.


def save_user(**user):
    print(user["name"])


save_user(id=1, name="John", age=22)

x = input("x: ")
# accepted input is always of type string
print(type(x))
# type() is used to tell the type(int, float, string, bool) of variable passed to it
y = int(x) + 1
# in the above case y = x + 1 is invalid because value of x is a string and
# a string cannot be added to integer i.e. 1. so we convert the type of x to
# integer by type conversion functions such as int(), float(), bool(), str()
print(f"y: {y}")
# bool()
# Python has a concept of truthy and falsy values i.e. values that are boolean true
# and values that are boolean false
# boolean false values -> "", 0, None
# rest all avlues are boolean trues

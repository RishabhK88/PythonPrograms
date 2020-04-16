# Dictionaries are collection of key-value pairs
point = {"x": 1, "y": 2}
# We can also use dictionaries usind dict() function
point = dict(x=1, y=2)
print(point["x"])
point["x"] = 3
print(point)
point["z"] = 4
print(point)
# If we print value of key which does not exist in dictionary, we get an error
# So we can check its existence and then print, for example
if "a" in point:
    print(point["a"])
# Or we can use get() method, so if key does not exist, it return none by default.
# We can also add default value as second parameter which will be shown if key doesnt
# exist
print(point.get("a", 0))
# We use del to delete
del point["x"]
print(point)
# We can loop over dictionaries as follows
for key in point:
    print(key, point[key])

# Another way to iterate over dictionaries is
for key, value in point.items():
    print(key, value)

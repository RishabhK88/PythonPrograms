import pickle
# Pickling
cars = ["Audi", "BMW", "Ferrari"]
file = "mycar.pkl"
f = open(file, "wb")
pickle.dump(cars, f)
f.close()


# Depickle
file = "mycar.pkl"
f = open(file, "rb")
mycar = pickle.load(f)
print(mycar)
print(type(mycar))

# Module used to pack in binary file

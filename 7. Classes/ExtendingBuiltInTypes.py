# We can also extend built in data types. for example we can create a class "Text"
# and have it inherit from class string(str). So Text will get all methods of class
# string and we can also add additional methods.


class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
print(text.duplicate())
print(text.lower())


class TrackableList(list):
    def append(self, object):
        print("Append Called")
        super().append(object)


list = TrackableList()
list.append("1")

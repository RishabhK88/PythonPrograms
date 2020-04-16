# prefixing methods or attributes with double underscore makes them private that is
# difficult to access through the outside world. Technically they can still be
# accessed


class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag, 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        iter(self.__tags)


cloud = TagCloud()
print(cloud.__dict__)
print(cloud._TagCloud__tags)

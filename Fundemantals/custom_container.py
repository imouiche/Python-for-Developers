
#  building a dictonary container


class TagCloud:
    def __init__(self):
        self.__tags = {}  # __ to make it a private member

    def add(self, tag):
        # pass 0 as default value of key = tag
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        # iter if built-in func which allows us to get 1 item at a time
        return iter(self.__tags)


cloud = TagCloud()
cloud['Java'] = 10
len(cloud)
cloud.add('python')
cloud.add('Python')
cloud.add('Python')

print(cloud.__tags["Python"])

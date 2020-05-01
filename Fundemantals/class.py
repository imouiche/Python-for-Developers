class Point:
    default_color = "red"  # class attribute

    # define a counstructor
    def __init__(self, x, y):  # all __sthg__() are called magic methods automatically called by python interpreter we create a new obj
        self.x = x  # instance attribute
        self.y = y

    # define method at the class level
    @classmethod
    def zero(cls):
        # same like using Point(0, 0), cls is by convention and could be something something else
        return cls(0, 0)

     # passing self here is not mandatory as cyphone interpreter does it for us

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(3, 2)
another = Point(1, 1)
print(point + another)
point = Point.zero()
print(point)
# print(point.default_color)
# print(Point.default_color)
# point.draw()


# another.draw()

print(isinstance(point, Point))

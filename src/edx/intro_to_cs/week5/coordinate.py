
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return 'Coordinate(' + str(self.x) + ',' + str(self.y) + ')'


c = Coordinate(0, 3)
cCopy = Coordinate(0, 3)
d = Coordinate(4, 0)
# print(c.x)
# print(c)
# print(type(c))
print(c == cCopy)
print(c != d)

print(repr(c))
print(c)
print(eval(repr(c)))
print(eval(repr(c)) == c)

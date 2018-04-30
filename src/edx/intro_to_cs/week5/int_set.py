class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
        return_set = intSet()
        for val in self.vals:
            if other.member(val):
                return_set.insert(val)
        return return_set

    def __len__(self):
        return len(self.vals)


first_set = intSet()
first_set.insert(1)
first_set.insert(3)
first_set.insert(3)
first_set.insert(2)
second_set = intSet()
second_set.insert(2)
second_set.insert(4)
second_set.insert(1)
common_set = intSet()
common_set.insert(1)
common_set.insert(2)


print(second_set)
print(first_set)

print((str(first_set) == str(second_set)) == False)
print(str(first_set.intersect(second_set)) == str(common_set))
print(len(first_set.intersect(second_set)) == 2)


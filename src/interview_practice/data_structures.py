#data structures

#array lists
import numpy as np
array = np.zeros((4), dtype=float)
array[2] = 2
# print(array)

#hash tables
dict = {"abc":"cde", "ab":"cd"}
# print(dict["ab"])
dict["a"] = "efghi"
# print(dict)

#linked list
import collections as coll
dll = coll.deque()
dll.extend("a")
print(dll[0])
print(dll[-1])
dll.extend("b")
dll.extendleft("c")
print(dll[-2])
print(dll)



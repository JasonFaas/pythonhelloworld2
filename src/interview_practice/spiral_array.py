#spiral_array

#1
#1

#2
#1 2
#4 3

#3
#1 2 3
#8 9 4
#7 6 5
import numpy as np

def spiral_array(size, start_value= 1):
    if size >= 3:
        nested_array = spiral_array(size - 2, start_value + (size - 1) * 4)

    array = np.zeros((size, size), dtype=int)
    if size == 1:
        array[0, 0] = start_value
    elif size == 2:
        array[0, 0] = start_value
        array[0, 1] = start_value + 1
        array[1, 1] = start_value + 2
        array[1, 0] = start_value + 3
    else:
        for row_itr in range(size-2):
            for col_itr in range(size-2):
                array[1 + row_itr, 1 + col_itr] = nested_array[row_itr, col_itr]
        for top_row_itr in range(size - 1):
            array[0, top_row_itr] = start_value + top_row_itr
            array[top_row_itr, size - 1] = start_value + size - 1 + top_row_itr
            array[size - 1, size - 1 - top_row_itr] = start_value + size - 1 + size - 1 + top_row_itr
            array[size - 1 - top_row_itr, 0] = start_value + (size - 1) * 3 + top_row_itr
    return array


print(spiral_array(1))
print(spiral_array(2))
print(spiral_array(3))
print(spiral_array(4))
print(spiral_array(5))
print(spiral_array(6))
# print(spiral_array(500))


import numpy as np

height = (1.73, 1.71, 1.55, 1.60, 1.87)
weight = (55, 66, 77, 88, 75)

np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight / np_height ** 2

print(bmi)
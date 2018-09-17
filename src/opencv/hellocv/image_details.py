import cv2
import numpy as np


img = cv2.imread('dragonball1.jpg')
img2 = cv2.imread('Charmand_Razor_Leaf.jpg')


means = cv2.mean(img)
print(int(means[0]))
print(int(means[1]))
print(int(means[2]))
means = cv2.mean(img2)
print(int(means[0]))
print(int(means[1]))
print(int(means[2]))

# cv2.imshow('Charmander', img)
# cv2.waitKey(0) & 0xFF
# cv2.destroyAllWindows()

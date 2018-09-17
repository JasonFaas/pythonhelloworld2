import cv2
import numpy as np


img = cv2.imread('dragonball1.jpg', 0)

hist = cv2.calcHist([img], [0], None, [3], [0, 256])
cv2.normalize(hist, hist).flatten()
print(hist)

cv2.imshow('Charmander', img)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

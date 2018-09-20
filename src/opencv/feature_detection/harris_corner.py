import numpy as np
import cv2 as cv

img = cv.imread('../resources/SuperMarioMaker-Wallpaper-1366x768.png')
img = cv.imread('../resources/z_320x480.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv.cornerHarris(gray, 2, 3, 0.04)

dst = cv.dilate(dst, None)

img[dst > 0.01 * dst.max()] = [255, 100, 100]

cv.imshow('dst', img)
cv.waitKey(0) & 0xFF
cv.destroyAllWindows()

import cv2 as cv
import numpy as np

img = cv.imread('../resources/small_insert.jpg')
hue, sat, val = cv.split(cv.cvtColor(img, cv.COLOR_BGR2HSV))
_, sat_binary = cv.threshold(sat, 256/2, 255, cv.THRESH_BINARY)
_, val_binary = cv.threshold(val, 256/2, 255, cv.THRESH_BINARY)
_, hue = cv.threshold(hue, 180 - 20, 255, cv.THRESH_TOZERO_INV)
hue = cv.bitwise_and(hue, hue, mask=sat_binary)
hue = cv.bitwise_and(hue, hue, mask=val_binary)
cv.imshow('original', img)
cv.imshow('hue', hue)

max_value = 180
while True:
    # Best found 35, 150
    # Note that quick guess for that background is (187, 84, 50) on (360, 100, 100) scale
    lower_bound = np.random.randint(max_value / 2)
    upper_bound = np.random.randint(max_value / 2) + max_value / 2
    print("bounds:" + str(lower_bound) + ":" + str(upper_bound))
    edges = cv.Canny(hue, lower_bound, upper_bound)
    cv.imshow('edges', edges)
    if cv.waitKey(1000) & 0xFF == 27:
        break

cv.destroyAllWindows()

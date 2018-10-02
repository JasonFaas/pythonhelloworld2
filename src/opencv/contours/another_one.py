import numpy as np
import cv2 as cv

img = cv.imread('opencv_frame_5_0.png')
blue, green, red = cv.split(img)
hue, sat, val = cv.split(cv.cvtColor(img, cv.COLOR_BGR2HSV))
cv.imshow('org', img)

kernel_1 = np.ones((1, 1), np.uint8)
kernel_3 = np.ones((3, 3), np.uint8)
kernel_5 = np.ones((5, 5), np.uint8)
kernel_9 = np.ones((9,9), np.uint8)


# get mask of checkerboard

_, sat = cv.threshold(sat, 50, 255, cv.THRESH_BINARY)
not_sat = cv.bitwise_not(sat)
not_sat_close_3 = cv.morphologyEx(not_sat, cv.MORPH_CLOSE, kernel_3, iterations=3)
val_adp_thr_blk = cv.adaptiveThreshold(val, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 51, 25)
val_adp_thr_wht = cv.adaptiveThreshold(val, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 51, -25)
both = cv.add(val_adp_thr_blk, val_adp_thr_wht)

open_9 = cv.morphologyEx(both, cv.MORPH_OPEN, kernel_3, iterations=3)

cv.imshow('not_sat_close_3', not_sat_close_3)
cv.imshow('val_adp_thr_blk', val_adp_thr_blk)
cv.imshow('val_adp_thr_wht', val_adp_thr_wht)
cv.imshow('both', both)
cv.imshow('open_9', open_9)

# final = cv.bitwise_and(open_9, not_sat_close_3)

final = cv.medianBlur(open_9, 201)
final = cv.dilate(final, kernel_5, iterations=9)
cv.imshow('final', final)

mask = cv.bitwise_and(img, img, mask=final)
cv.imshow('mask', mask)

cv.waitKey(0)

cv.destroyAllWindows()
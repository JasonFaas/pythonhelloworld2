import numpy as np
import cv2 as cv

img = cv.imread('opencv_frame_5_0.png')
blue, green, red = cv.split(img)
hue, sat, val = cv.split(cv.cvtColor(img, cv.COLOR_BGR2HSV))

_, sat_thresh = cv.threshold(sat, 35, 255, cv.THRESH_BINARY)
kernel_1 = np.ones((1, 1), np.uint8)
kernel_3 = np.ones((3, 3), np.uint8)
kernel_5 = np.ones((5, 5), np.uint8)
kernel_9 = np.ones((9,9), np.uint8)
sat_thresh_2 = cv.morphologyEx(sat_thresh, cv.MORPH_OPEN, kernel=kernel_5, iterations=2)
sat_thresh_3 = cv.dilate(sat_thresh_2, kernel=kernel_5, iterations=3)


cv.imshow('org', img)
cv.imshow('val', val)
cv.imshow('sat', sat)
cv.imshow('sat_thresh', sat_thresh)
# cv.imshow('sat_thresh_2', sat_thresh_2)
cv.imshow('sat_thresh_3', sat_thresh_3)
not_sat_thresh_3 = cv.bitwise_not(sat_thresh_3)
cv.imshow('not_sat_thresh_3', not_sat_thresh_3)



# TODO reenable corners
# corners = cv.preCornerDetect(val, 5)
# cv.imshow('corners0', corners)
# final = cv.erode(corners, kernel_1)
# cv.imshow('corners1', final)
# _, final = cv.threshold(final, 1, 255, cv.THRESH_BINARY)
# cv.imshow('corners2', final)
# sat_thresh_3 = cv.dilate(sat_thresh_3, kernel_9, iterations=5)
# final = cv.bitwise_and(final, final, mask=not_sat_thresh_3)
# cv.imshow('corners3', final)



# get mask of checkerboard

dilated_val = cv.dilate(val, kernel_9, iterations=9)
cv.imshow('dilated_val', dilated_val)
_, dilated_val_bin = cv.threshold(dilated_val, 150, 255, cv.THRESH_BINARY)
cv.imshow('dilated_val_bin', dilated_val_bin)
combine = cv.bitwise_and(dilated_val_bin, not_sat_thresh_3)
cv.imshow('combine', combine)

combine2 = cv.erode(combine, kernel_5, iterations=6)
# combine2 = cv.dilate(combine2, kernel_5, iterations=3)

cv.imshow('combine2', combine2)

# dilated_not_sat_thresh = cv.dilate(not_sat_thresh, kernel_9, iterations=5)
# combine = cv.bitwise_and(dilated_val, dilated_not_sat_thresh)
# cv.imshow('combine', combine)

cv.waitKey(0)

cv.destroyAllWindows()
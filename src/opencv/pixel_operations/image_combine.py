import numpy as np
import cv2 as cv

x = np.uint8([250])
y = np.uint8([10])

# print(cv.add(x, y))

# print(x+y)

a = cv.imread('../resources/a.jpg')
b = cv.imread('../resources/b.jpg')

#merge 2 images with be having greater emphasis
dst = cv.addWeighted(b, .5, a, .5, 0)
cv.imshow('dst', dst)

#putting image c on top of image b, negating background color
c = cv.imread('../resources/small_insert.jpg')
rows, cols, channels = c.shape
b_roi = b[0:rows, 0:cols]
c_as_hsv = cv.cvtColor(c, cv.COLOR_BGR2HSV)
c_h, c_s, c_v = cv.split(c_as_hsv)

hue_min = 90
hue_max = 110
hue_ret, hue_mask_min = cv.threshold(c_h, hue_min, 255, cv.THRESH_BINARY)
hue_ret, hue_mask_max = cv.threshold(c_h, hue_max, 255, cv.THRESH_BINARY_INV)
hue_mask = cv.bitwise_and(hue_mask_min, hue_mask_max)

sat_ret, sat_mask = cv.threshold(c_s, 210, 255, cv.THRESH_BINARY)

val_ret, val_mask = cv.threshold(c_s, 170, 240, cv.THRESH_BINARY)
val_ret, val_mask = cv.threshold(val_mask, 1, 255, cv.THRESH_BINARY)
final_mask = cv.bitwise_and(hue_mask, sat_mask)
final_mask = cv.bitwise_and(final_mask, val_mask)
final_invert_mask = cv.bitwise_not(final_mask)

b_after_mask = cv.bitwise_and(b_roi, b_roi, mask=final_mask)
c_after_mask = cv.bitwise_and(c, c, mask=final_invert_mask)
b_c_dst = cv.add(b_after_mask, c_after_mask)
b[0:rows, 0:cols] = b_c_dst

cv.imshow('f_m',final_mask)
cv.imshow('f_i_m',final_invert_mask)
cv.imshow('c_after_mask',c_after_mask)
cv.imshow('b_after_mask',b_after_mask)
cv.imshow('b_c_combined',b)



cv.waitKey(0) & 0xFF
cv.destroyAllWindows()
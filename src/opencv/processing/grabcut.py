import numpy as np
import cv2 as cv

img = cv.imread('../resources/SuperMarioMaker-Wallpaper-1366x768.png')
img_orig = img.copy()

# img_mask = cv.imread('../resources/small_insert_mask.jpg')
# hue, sat, val = cv.split(cv.cvtColor(img_mask, cv.COLOR_BGR2HSV))
# _, sat_thresh = cv.threshold(sat, 70, 255, cv.THRESH_BINARY_INV)
# _, val_thresh = cv.threshold(val, 40, 255, cv.THRESH_BINARY_INV)
# prep_mask = cv.bitwise_or(sat_thresh, val_thresh)
# cv.imshow('sat', sat)
# cv.imshow('val', val)
# cv.imshow('sat_thresh', sat_thresh)
# cv.imshow('val_thresh', val_thresh)
# cv.imshow('prep_mask', prep_mask)


img_shape = img.shape[:2]
mask = np.zeros(img_shape, np.uint8)

bgdModel = np.zeros((1,65), np.float64)
fgdModel = np.zeros((1,65), np.float64)

# small insert rect
rect = (5, 5, img_shape[1]-10, img_shape[0]-10)

# mario rect
rect = (122, 552, 195-122, 646-552)

cv.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

cv.imshow('result', img)
cv.imshow('img_orig', img_orig)
cv.waitKey(0) & 0xFF
cv.destroyAllWindows()

print(mask)

import cv2 as cv
import numpy as np

big_img = cv.imread('../resources/a_1280x720.jpg', 0)

# small_img = cv.imread('../resources/d_320x480.jpg', 0)
# small_img = small_img[int(s_w * .1):int(s_w * .9),
#             int(s_h * .1):int(s_h * .9)]

s_w, s_h = big_img.shape
small_img = big_img[int(s_w * .4):int(s_w * .6),
            int(s_h * .4):int(s_h * .6)]
w, h = small_img.shape



# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
cv.imshow('org', big_img)
for meth in methods:
    big_img_copy = big_img.copy()
    method = eval(meth)

    res = cv.matchTemplate(big_img_copy, small_img, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + h, top_left[1] + w)

    cv.rectangle(big_img_copy, top_left, bottom_right, 255, 2)

    cv.imshow(meth, big_img_copy)

cv.imshow("small", small_img)
cv.waitKey(0) & 0xFF
cv.destroyAllWindows()

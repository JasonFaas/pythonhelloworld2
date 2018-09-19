import numpy as np
import cv2 as cv
# img = cv.imread('../resources/f_320x480.jpg')
img = cv.imread('../resources/small_insert.jpg')
cv.imshow("original", img)

blur_width = 11
kernel = np.ones((blur_width, blur_width), np.float32) / (blur_width ** 2)
average_blur = cv.filter2D(img, -1, kernel)
cv.imshow("average_blur", average_blur)

g_blur = cv.GaussianBlur(img, (blur_width, blur_width), 0)
cv.imshow("g_blur", g_blur)

median_blur = cv.medianBlur(img, blur_width)
cv.imshow("median_blur", median_blur)

bilateral_filter = cv.bilateralFilter(img, blur_width, 75, 75)
cv.imshow("bilateral_filter", bilateral_filter)


cv.waitKey(0) & 0xFF
cv.destroyAllWindows()
import cv2 as cv

img = cv.imread('../resources/threshold.jpg', cv.IMREAD_GRAYSCALE)
ret, img2 = cv.threshold(img, 80, 255, cv.THRESH_BINARY)
ret, img3 = cv.threshold(img, 120, 255, cv.THRESH_BINARY_INV)

cv.imshow('original', img)
cv.imshow('modded', img2)
cv.imshow('modded_inv', img3)
region = cv.bitwise_and(img2, img3)
cv.imshow('desired', region)

cv.waitKey(0) & 0xFF
cv.destroyAllWindows()
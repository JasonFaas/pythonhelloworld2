import cv2 as cv
import numpy as np

img = cv.imread('../resources/320x480-Wallpaper-110.jpg')
cv.imshow('org', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
hue, sat, val = cv.split(hsv)
cv.imshow('value', val)
cv.imshow('sat', sat)
_, t1 = cv.threshold(sat, 30, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
cv.imshow('t1', t1)
_, t2 = cv.threshold(val, 30, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
cv.imshow('t2', t2)
t12 = cv.bitwise_or(t1, t2)
cv.imshow('t12', t12)

# noise removal
kernel = np.ones((3,3), np.uint8)
opening = cv.morphologyEx(t12, cv.MORPH_OPEN, kernel, iterations=2)
cv.imshow('opening', opening)

# sure background area
sure_bg = cv.dilate(opening, kernel, iterations=3)
cv.imshow('sure_bg', sure_bg)

#Finding sure foreground area
dist_transform = cv.distanceTransform(opening, cv.DIST_L2, 5)
_, sure_fg = cv.threshold(dist_transform, 0.3 * dist_transform.max(), 255, 0)
cv.imshow('sure_fg', sure_fg)

#finding unknown region
sure_fg = np.uint8(sure_fg)
# unknown = cv.subtract(sure_bg, sure_fg)
unknown = cv.bitwise_and(sure_bg, sure_fg)
cv.imshow('unknown', unknown)

#marker labelling
_, markers = cv.connectedComponents(unknown)
# cv.imshow('markers1', markers)
#add one to all labels so that sure background is not 0, but 1
markers = markers+1
# cv.imshow('markers2', markers)
#now, mark the region of unknown with zero
markers[unknown==255] = 0
# cv.imshow('markers3', markers)



# attempting to locate circles with hough circles
original_copy = img.copy()
img_circles = unknown.copy()
circles_blur = cv.blur(img_circles, (11, 11))
cv.imshow("circles_blur3", circles_blur)
# circles_blur = cv.blur(img_circles, (31, 31))
# cv.imshow("circles_blur31", circles_blur)
circles = cv.HoughCircles(circles_blur, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=5, maxRadius=100)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv.circle(original_copy,(i[0],i[1]),i[2],(0,0,0),2)
    # draw the center of the circle
    cv.circle(original_copy,(i[0],i[1]),2,(255,255,255),3)
cv.imshow("original_copy_with_circles", original_copy)





cv.waitKey(0) & 0xFF
cv.destroyAllWindows()

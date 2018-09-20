import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('../resources/320x480-Wallpaper-110.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
hue, sat, val = cv.split(hsv)
_, t1 = cv.threshold(sat, 30, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
_, t2 = cv.threshold(val, 30, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
t12 = cv.bitwise_or(t1, t2)


hist = cv.calcHist([hue],[0],None,[180],[0,180])
hist2 = cv.calcHist([hue],[0],t12,[180],[0,180])
# hist,bins = np.histogram(hue.ravel(),180,[0,180])
# plt.hist(hue.ravel(),100,[0,180])
plt.plot(hist,color='b')
plt.plot(hist2,color='r')
plt.show()



final_display = img.copy()
cv.imshow('org', img)

cv.imshow('gray', gray)
cv.imshow('value', val)
cv.imshow('sat', sat)
cv.imshow('t1', t1)
cv.imshow('t2', t2)
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
all_circles = np.zeros((1,3), dtype=int)
# print(all_circles)
for i in reversed(range(4, 12)):
    img_circles = unknown.copy()
    circles_blur = cv.blur(img_circles, (i * 2 + 1, i * 2 + 1))
    cv.imshow("circles_blur_" + str(i), circles_blur)
    circles = cv.HoughCircles(circles_blur, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=i*4, maxRadius=i * 10)
    if type(circles) != type(None) and len(circles) > 0 and circles[0,0,0] != 0:
        circles = np.uint16(np.around(circles))
        circles_formated = circles[0, :]
        for i in circles_formated:
            # do not draw circle if another circle is within 30 pixels
            circles_prep = all_circles - i
            circles_distance = (circles_prep[:, 0] ** 2 + circles_prep[:, 1] ** 2) ** .5
            distance_ = np.sum(circles_distance < 30) > 0
            if distance_ > 0:
                continue

            # draw the outer circle
            cv.circle(final_display, (i[0], i[1]), i[2], (0, 0, 0), 2)
            # draw the center of the circle
            cv.circle(final_display, (i[0], i[1]), 2, (255, 255, 255), 3)
        all_circles = np.append(all_circles, circles_formated, axis=0)
cv.imshow("original_copy_with_circles", final_display)





cv.waitKey(0) & 0xFF
cv.destroyAllWindows()

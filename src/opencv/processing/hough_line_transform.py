import cv2 as cv
import numpy as np

img = cv.imread('../resources/SuperMarioMaker-Wallpaper-1366x768.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2HSV)
edges = cv.Canny(gray, 50, 150, apertureSize = 3)
cv.imshow('org', img)

lines = cv.HoughLines(edges, 1, np.pi / 180, 200)
img_long_lines = img.copy()
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))

    cv.line(img_long_lines,(x1, y1),(x2,y2), (0, 0, 255), 2)
cv.imshow("long_lines", img_long_lines)

img_short_lines = img.copy()
lines = cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength=100,maxLineGap=10)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv.line(img_short_lines,(x1,y1),(x2,y2),(255,50,50),2)
cv.imshow("short_lines", img_short_lines)


cv.waitKey(0) & 0xFF
cv.destroyAllWindows()
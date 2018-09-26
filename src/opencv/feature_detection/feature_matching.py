import numpy as np
import cv2 as cv

img1 = cv.imread('../resources/a_db_limited_rect.jpeg')
# img1 = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
# hue1, _, _ = cv.split(cv.cvtColor(img1, cv.COLOR_BGR2HSV))
img2 = cv.imread('../resources/a_db_more.jpg')
# img2 = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
# hue2, _, _ = cv.split(cv.cvtColor(img2, cv.COLOR_BGR2HSV))


orb = cv.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x:x.distance)
print(len(matches))
img3 = cv.drawMatches(img1, kp1, img2, kp2, matches[:10], outImg=None, flags=2)


#TODO investigate SIFT options
# sift = cv.xfeatures2d.SIFT_create()
# kp1, des1 = sift.detectAndCompute(img1, None)
# kp2, des2 = sift.detectAndCompute(img2, None)
# bf = cv.BFMatcher()
# matches = bf.knnMatch(des1, des2, k=2)
# good = []
# for m,n in matches:
#     if m.distance < 0.75 * n.distance:
#         good.append([m])
# img4 = cv.drawMatchesKnn(img1, kp1, img2, kp2, good, flags=2)


cv.imshow("1 org", img1)
cv.imshow("2 org", img2)
cv.imshow("3 res", img3)
cv.waitKey(0) & 0xFF
cv.destroyAllWindows()

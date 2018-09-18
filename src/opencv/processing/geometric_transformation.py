import cv2 as cv
import numpy as np

img = cv.imread('../resources/a_320x480.jpg')

# Scaling
# TWO OPTIONS
res_1 = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)
height, width, _ = img.shape
res_2 = cv.resize(img, (2*width, 2*height), interpolation=cv.INTER_CUBIC)

# cv.imshow("resize_2", res_2)
# cv.imshow("resize_1", res_1)
cv.imshow("original", img)


# Translation
M = np.float32([[1, 0, 100], [0, 1, 50]])
trans_dst = cv.warpAffine(img, M, (width, height))

cv.imshow("translation", trans_dst)


# Rotation
M = cv.getRotationMatrix2D(center=(width / 2, height / 2), angle=45, scale=1)
rotation_dst = cv.warpAffine(img, M, (width, height))

cv.imshow('Rotation', rotation_dst)


#Affine Transformation
pts1 = np.float32([[50, 50],[200, 50], [50,200]])
pts2 = np.float32([[10, 100],[200, 50], [100,250]])
M = cv.getAffineTransform(pts1, pts2)
affine_transformation_dst = cv.warpAffine(img, M, (width, height))
cv.imshow("Affine Transformation", affine_transformation_dst)


#Perspective Transformation
img = cv.imread('../resources/a_1280x720.jpg')
height, width, _ = img.shape
pts1 = np.float32([[1054, 98],[1144, 35],[1053, 277],[1145, 254]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv.getPerspectiveTransform(pts1, pts2)
perspective_transformation_dst = cv.warpPerspective(img, M, (300, 300))
cv.imshow('perspective_transformation_dst', perspective_transformation_dst)

cv.waitKey(0) & 0xFF

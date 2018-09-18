import numpy as np
import cv2 as cv

show_img = False

img = cv.imread('../resources/Charmand_Razor_Leaf.jpg')
px = img[100, 100]
print(px)

blue = img[100, 100, 0]
print(blue)

img[100, 100] = [255, 255, 255]
print(px)


print(img.item(10, 10, 2))

img.itemset((10, 10, 2), 100)
print(img.item(10, 10, 2))


print(img.shape)

print(img.size)
img_shape = img.shape
print(img_shape[0] * img_shape[1] * img_shape[2])

print(img.dtype)

squirtle = img[int(img_shape[0] / 3):int(img_shape[0] * 3 / 4),
           int(img_shape[1] / 4): int(img_shape[1] / 2) ]

cv.imshow("squirtle", squirtle)

img[0:squirtle.shape[0], 0:squirtle.shape[1]] = squirtle
cv.imshow("whole", img)

#expensive call
b,g,r = cv.split(img)
img_reverse = cv.merge((r,g,b))
cv.imshow("reverse", img_reverse)

b = img[:,:,0]
#cheap call
img_reverse[:,:,1] = 0
cv.imshow("reverse_no_green", img_reverse)

a = cv.copyMakeBorder(img, 20, 20, 20, 20, cv.BORDER_REPLICATE)
b = cv.copyMakeBorder(img, 20, 20, 20, 20, cv.BORDER_REFLECT)
c = cv.copyMakeBorder(img, 20, 20, 20, 20, cv.BORDER_REFLECT_101)
d = cv.copyMakeBorder(img, 20, 20, 20, 20, cv.BORDER_WRAP)
f = cv.copyMakeBorder(img, 20, 20, 20, 20, cv.BORDER_CONSTANT, value=[0, 100, 0])

cv.imshow('gray', img)
cv.imshow('Replicate', a)
cv.imshow('Reflect', b)
cv.imshow('Reflect_101', c)
cv.imshow('Wrap', d)
cv.imshow('Constant', f)
#
# plt.show()
cv.waitKey(0) & 0xFF


import cv2
import numpy as np

# img = cv2.imread('Charmand_Razor_Leaf.jpg')
img = cv2.imread('dragonball1.jpg')
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height, width, depth = np.shape(img)

for w in range(0, width):
    for h in range(0, int(3 * height/4)):
        # for d in range(1, 3):
        img[h][w][0] = 200
        img[h][w][2] = 100

cv2.line(img, (10, 10), (int(height/2), int(width/3)), (100, 255, 100), 4)
cv2.rectangle(img, (0, 30), (100,100), (0,0,255), 3)

cv2.imshow('Charmander', img)
# cv2.imshow('Charmander_Gray', gray_img)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

# print(np.shape(gray_img))

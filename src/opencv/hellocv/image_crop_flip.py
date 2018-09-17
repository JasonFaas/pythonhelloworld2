import cv2
import numpy as np


img = cv2.imread('dragonball1.jpg')

height, width, depth = np.shape(img)
if height % 4 != 0 or width % 4 != 0:
    print(str(height) + " or " + str(width) + " invalid")
    exit()



for w in range(0, int(width/2)):
    for h in range(0, int(height/2)):
        img[height - h - 1][w][0] = img[h][w][0]
        img[height - h - 1][w][1] = img[h][w][1]
        img[height - h - 1][w][2] = img[h][w][2]
        img[h][width - w - 1][0] = img[h][w][0]
        img[h][width - w - 1][1] = img[h][w][1]
        img[h][width - w - 1][2] = img[h][w][2]
        img[height - h - 1][width - w - 1][0] = img[h][w][0]
        img[height - h - 1][width - w - 1][1] = img[h][w][1]
        img[height - h - 1][width - w - 1][2] = img[h][w][2]


cv2.imshow('Charmander', img)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

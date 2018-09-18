import cv2 as cv
import numpy as np

img = cv.imread("../resources/small_insert.jpg")
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
hue, _, _ = cv.split(hsv)
hue_blur = cv.medianBlur(src=hue, ksize=3)


constant = 3
neighborhood = 11
while True:
    hue_thresh = cv.adaptiveThreshold(hue_blur,
                                      255,
                                      cv.ADAPTIVE_THRESH_MEAN_C,
                                      cv.THRESH_BINARY,
                                      neighborhood,
                                      -1 * constant)
    hue_thresh_inv = cv.adaptiveThreshold(hue_blur,
                                          255,
                                          cv.ADAPTIVE_THRESH_MEAN_C,
                                          cv.THRESH_BINARY_INV,
                                          neighborhood,
                                          constant)

    hue_and = cv.bitwise_and(hue_thresh, hue_thresh_inv)
    hue_and_not = cv.bitwise_not(cv.bitwise_or(hue_thresh_inv, hue_thresh))

    cv.imshow("original", img)
    cv.imshow("hue_thresh", hue_thresh)
    cv.imshow("hue_thresh_inv", hue_thresh_inv)
    cv.imshow("hue_and", hue_and)
    cv.imshow("hue_and_not", hue_and_not)



    key_press = cv.waitKey(0) & 0xFF
    if key_press == 27:
        break
    elif key_press == ord('u'):
        constant += 1
        print("neighborhood and constant:")
        print(str(neighborhood) + " " + str(constant))
    elif key_press == ord('i'):
        constant -= 1
        print("neighborhood and constant:")
        print(str(neighborhood) + " " + str(constant))
    elif key_press == ord('o'):
        neighborhood += 2
        print("neighborhood and constant:")
        print(str(neighborhood) + " " + str(constant))
    elif key_press == ord('p'):
        neighborhood -= 2
        print("neighborhood and constant:")
        print(str(neighborhood) + " " + str(constant))


cv.destroyAllWindows()

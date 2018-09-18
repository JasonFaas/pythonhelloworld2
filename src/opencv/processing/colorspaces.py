import cv2 as cv
import numpy as np

capture = cv.VideoCapture(0)

while True:
    # read frame
    _, frame = capture.read()

    # convert color to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define hsv range for green sunglasses
    lower_bound = np.array([100/2, 50, 50])
    upper_bound = np.array([140/2, 255, 255])

    mask = cv.inRange(hsv, lowerb=lower_bound, upperb=upper_bound)

    result = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow("result", result)
    if cv.waitKey(5) & 0xFF == 27:
        break

cv.destroyAllWindows()


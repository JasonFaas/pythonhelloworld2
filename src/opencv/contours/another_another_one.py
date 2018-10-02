import numpy as np
import cv2 as cv

img_orig = cv.imread('opencv_frame_5_0.png') #Good
# img_orig = cv.imread('more_examples/opencv_frame_5_1.png') #Good
# img_orig = cv.imread('more_examples/opencv_frame_7_1.png')
# img_orig = cv.imread('more_examples/opencv_frame_7_0.png')
# img_orig = cv.imread('more_examples/opencv_frame_0_1.png')
# img_orig = cv.imread('more_examples/opencv_frame_0_0.png')
img = img_orig.copy()
blue, green, red = cv.split(img)
hue, sat, val = cv.split(cv.cvtColor(img, cv.COLOR_BGR2HSV))
cv.imshow('org', img)

kernel_1 = np.ones((1, 1), np.uint8)
kernel_3 = np.ones((3, 3), np.uint8)
kernel_5 = np.ones((5, 5), np.uint8)
kernel_9 = np.ones((9,9), np.uint8)

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
board_width = 7
objp = np.zeros((board_width * board_width, 3), np.float32)
objp[:,:2] = np.mgrid[0:board_width, 0:board_width].T.reshape(-1, 2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
img = img.copy()
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Find the chess board corners
ret, corners = cv.findChessboardCorners(gray, (board_width, board_width), None)
# If found, add object points, image points (after refining them)
if ret == True:
    objpoints.append(objp)
    corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
    imgpoints.append(corners)
    # Draw and display the corners
    cv.drawChessboardCorners(img, (board_width, board_width), corners2, ret)
    cv.imshow('img', img)



print(corners2)

# TODO put this into a verification
smallest_x = np.min(corners2[:, 0, 0])
smallest_y = np.min(corners2[:, 0, 1])
largest_x = np.max(corners2[:, 0, 0])
largest_y = np.max(corners2[:, 0, 1])
# print(smallest_x)
left_most_point = corners2[board_width ** 2 - board_width, 0]
# print(left_most_point)
# print(smallest_y)
top_most_point = corners2[0, 0]
# print(top_most_point)
# print(largest_x)
right_most_point = corners2[board_width - 1, 0]
# print(right_most_point)
# print(largest_y)
bottom_most_point = corners2[board_width ** 2 - 1, 0]
# print(bottom_most_point)
# print(top_most_point.reshape(2,-1).shape)
# cv.line(img, top_most_point.reshape(2,-1), right_most_point.reshape(2,-1), (255, 0, 0), thickness=5)

img_squares = img_orig.copy()
hue, sat, val = cv.split(cv.cvtColor(img_squares, cv.COLOR_BGR2HSV))
image_sums = np.zeros((6,2), dtype=np.int32)
for square in range(6):
    first_bad_format = corners2[0+board_width*square, 0]
    second_bad_format = corners2[1+board_width*square, 0]
    fourth_bad_format = corners2[7+board_width*square, 0]
    third_bad_format = corners2[7+1+board_width*square, 0]
    first = (first_bad_format[0], first_bad_format[1])
    second = (int(first[0] * 2 - second_bad_format[0]), int(first[1] * 2 - second_bad_format[1]))
    fourth = (fourth_bad_format[0], fourth_bad_format[1])
    third = (int(fourth[0] * 2 - third_bad_format[0]), int(fourth[1] * 2 - third_bad_format[1]))
    roi_corners = np.array([[first, second, third, fourth]], dtype=np.int32)

    # draw lines
    # cv.line(img, first, second, (255, 0, 0), thickness=5)
    # cv.line(img, second, third, (255, 255, 0), thickness=5)
    # cv.line(img, third, fourth, (255, 0, 255), thickness=5)
    # cv.line(img, fourth, first, (0, 0, 0), thickness=5)

    mask = np.zeros(sat.shape, dtype=np.uint8)
    # channel_count = sat.shape[2]
    channel_count = 1
    ignore_mask_color = (255,)*channel_count
    cv.fillPoly(mask, roi_corners, ignore_mask_color)
    masked_image = cv.bitwise_and(sat, mask)
    cv.imshow('just_focus_' + str(square), masked_image)
    image__sum = (masked_image > 60).sum()
    image_sums[square] = (square, image__sum)
    print(str(square) + "_" + str(image__sum))

def highlight_finger(square):
    first_bad_format = corners2[0+board_width*square, 0]
    second_bad_format = corners2[1+board_width*square, 0]
    fourth_bad_format = corners2[7+board_width*square, 0]
    third_bad_format = corners2[7+1+board_width*square, 0]
    first = (first_bad_format[0], first_bad_format[1])
    second = (int(first[0] * 2 - second_bad_format[0]), int(first[1] * 2 - second_bad_format[1]))
    fourth = (fourth_bad_format[0], fourth_bad_format[1])
    third = (int(fourth[0] * 2 - third_bad_format[0]), int(fourth[1] * 2 - third_bad_format[1]))

    # draw lines
    cv.line(img, first, second, (255, 0, 0), thickness=5)
    cv.line(img, second, third, (255, 255, 0), thickness=5)
    cv.line(img, third, fourth, (255, 0, 255), thickness=5)
    cv.line(img, fourth, first, (0, 255, 255), thickness=5)


from operator import itemgetter
image_sums = sorted(image_sums, key=itemgetter(1))
print(image_sums)
print(image_sums[-1][1])
is_finger_detected = image_sums[-1][1] > image_sums[-2][1] * 2
print(is_finger_detected)
if is_finger_detected:
    highlight_finger(image_sums[-1][0])

cv.imshow('with lines', img)
cv.waitKey(0)



cv.destroyAllWindows()
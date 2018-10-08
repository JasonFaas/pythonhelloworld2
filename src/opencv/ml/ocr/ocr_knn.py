
import numpy as np
import cv2 as cv

img = cv.imread('digits.png')
cv.imshow("img", img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#split for each image
cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]

x = np.array(cells)
print(x.shape)
cv.imshow("single", x[0,0])


train = x[:,:50].reshape(-1, 400).astype(np.float32)
test = x[:,50:100].reshape(-1, 400).astype(np.float32)
print(train.shape)

k = np.arange(10)
train_labels = np.repeat(k, 250)[:np.newaxis]
test_labels = train_labels.copy()

knn = cv.ml.KNearest_create()
knn.train(train, cv.ml.ROW_SAMPLE, train_labels)
ret, result, neighbours, dist = knn.findNearest(test, k=5)

matches = result.reshape(result.size)==test_labels
correct = np.count_nonzero(matches)
accuracy = correct*100.0/result.size
print("result:" + str(result.reshape(result.size)))
print(result.reshape(result.size).shape)
print("test_labels:" + str(test_labels))
print(test_labels.shape)
print(matches)
print("results:" + str(result.size))
print("correct:" + str(correct))
print("accuracy:" + str(accuracy))

cv.waitKey(0)
cv.destroyAllWindows()

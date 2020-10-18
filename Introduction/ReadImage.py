import cv2 as cv

img = cv.imread("../Images/Ronaldo-1.jpg", 0)
print(img)
cv.imshow("First Image", img)
cv.waitKey(delay=0)
import cv2 as cv

img = cv.imread("../Images/Ronaldo-1.jpg", 1)
cv.imshow("Old Image", img)
cv.waitKey(0)
cv.imwrite("New-Picture.png", img)

cv.waitKey(0)
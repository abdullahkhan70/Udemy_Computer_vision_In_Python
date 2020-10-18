import cv2 as cv

image = cv.imread("../Images/Ronaldo-1.jpg")

height, width, channels = image.shape

font = cv.FONT_HERSHEY_COMPLEX_SMALL
image = cv.putText(image, "Abdullah Khan!", (50, 370), font, 1, (255,0,0), 1, cv.LINE_8)

cv.imshow("Text!", image)

cv.waitKey(0)
cv.destroyAllWindows()
import cv2 as cv

image = cv.imread("../Images/Ronaldo-1.jpg")
height, width, channels = image.shape

image = cv.line(image, (0,0), (width, height), (255,0,0), thickness=5)

#Fill a Rectangle
image = cv.rectangle(image, (30,30), (512, 250), (0.0,255), -1)

image = cv.circle(image, (width // 2, height // 2), 40, (255,0,0), -1)

cv.imshow("Draw Geomatric Shapes!", image)

if cv.waitKey(0) & 0XFF == ord("q"):
    cv.destroyAllWindows()
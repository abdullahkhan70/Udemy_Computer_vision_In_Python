import cv2 as cv

face_detection = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv.imread("../Images/Team-ManU.jpg")
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
face = face_detection.detectMultiScale(gray_img, 1.1, 5)


for (x,y,w,h) in face:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 6)


cv.imshow("Image", img)
cv.waitKey(0)
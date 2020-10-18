import cv2 as cv

img = cv.imread("Lion_king.png")
eye_detection = cv.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

eye_detect = eye_detection.detectMultiScale(gray_img, 1.1, 4)

for (x,y,w,h) in eye_detect:
    cv.rectangle(img, (x,y), (x+w, y+h),(255,0,0), 5)
    cv.imshow("Eye Detection!", img)

cv.waitKey(0)

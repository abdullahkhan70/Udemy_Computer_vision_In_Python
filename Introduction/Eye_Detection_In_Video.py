import cv2 as cv


eye_detection = cv.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")
cap = cv.VideoCapture("../Videos/Eye-cap-1.mp4")
cap.set(3, 1024)
cap.set(4, 768)
# cap = cv.VideoCapture(0)
print(cap.get(3))
print(cap.get(4))

while cap.isOpened():
    ret, frame = cap.read()
    print(ret)
    gray_video = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    eye_detect = eye_detection.detectMultiScale(gray_video)

    for (x,y,w,h) in eye_detect:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0.0,255), 5)

    cv.imshow("Eye Detection In Video!", frame)

    if cv.waitKey(1) & 0XFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
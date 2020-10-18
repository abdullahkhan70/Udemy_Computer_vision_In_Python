import cv2 as cv

face_detection = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

cap = cv.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    # cv.imshow("Video is Playing!", frame)
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_detect = face_detection.detectMultiScale(gray_frame,1.1,4)

    for (x,y,w,h) in face_detect:
        cv.rectangle(frame, (x,y), (x+w, y+h),(0,255,0), 6)

        cv.imshow("Face Detection in Video!", frame)

    if cv.waitKey(1) & 0XFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()


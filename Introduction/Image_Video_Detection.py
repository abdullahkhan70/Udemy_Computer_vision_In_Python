import cv2 as cv

cap = cv.VideoCapture("../Videos/Face-Cap-2.mp4")

face_detection = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_detection = cv.CascadeClassifier("haarcascade_eye_tree_eyeglasses.xml")

while cap.isOpened():
    ret, frame = cap.read()
    gray_image = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_detect = face_detection.detectMultiScale(gray_image, 1.1, 4)
    eye_detect = eye_detection.detectMultiScale(gray_image)

    for (fx, fy, fw, fh) in face_detect:
        cv.rectangle(frame, (fx, fy), (fx+fw, fy+fh), (255, 0, 0), thickness=4)

        for (ex, ey, ew, eh) in eye_detect:
            cv.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), thickness=4)

        cv.imshow("Face and Eye Detection!", frame)

    if cv.waitKey(1) & 0XFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
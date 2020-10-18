import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    ref, frame = cap.read()
    gray_video = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("Convert Video Into GrayScale!", gray_video)

    if cv.waitKey(2) & 0XFF == ord("e") or cv.waitKey(2) & 0XFF == ord("E"):
        break

cap.release()
cv.destroyAllWindows()
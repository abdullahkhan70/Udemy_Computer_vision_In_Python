import cv2 as cv

cap = cv.VideoCapture("../Videos/Players.mp4")

while True:

    ret, frame = cap.read()
    cv.imshow("Video Frame", frame)

    if cv.waitKey(3) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
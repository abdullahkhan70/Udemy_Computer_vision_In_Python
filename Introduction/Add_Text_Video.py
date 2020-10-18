import cv2 as cv

cap = cv.VideoCapture("../Videos/Face-Cap-3.mp4")

while cap.isOpened():
    ret, frame = cap.read()

    if ret == True:
        font = cv.FONT_HERSHEY_SIMPLEX
        text = "Abdullah Khan Personal Video!"
        cv.putText(frame, text, (15, 265), font, 1, (0,255,255), 2, cv.LINE_AA)
        cv.imshow("Text in Video!", frame)

    if cv.waitKey(1) & 0XFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
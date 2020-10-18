import cv2 as cv

video = cv.VideoCapture(0)
print(video.isOpened())

while (video.isOpened()):
    ret, frame = video.read()
    ret = video.set(cv.CAP_PROP_FRAME_WIDTH, 320)
    video_gray = cv.cvtColor(frame, cv.COLOR_BGR2Luv)

    cv.imshow("Video Properties!", video_gray)

    # Get the frame height and width:
    print("Height:  "+ str(video.get(cv.CAP_PROP_FRAME_HEIGHT)))
    print("Width: " + str(video.get(cv.CAP_PROP_FRAME_WIDTH)))

    if cv.waitKey(1) & 0XFF == ord("e"):
        break

video.release()
cv.destroyAllWindows()

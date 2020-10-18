import cv2 as cv

video = cv.VideoCapture(0)
FourCC_ = cv.VideoWriter_fourcc(*"XVID")
output = cv.VideoWriter("my_video.avi", FourCC_,30.0, (640, 480))

while (video.isOpened()):
    # ret means that whether it is capturing our video...
    ret, frame = video.read()
    if (ret == False):
        print("The video can not be playable!")
        break
    else:
        output.write(frame)

        cv.imshow("Video Capturing Mode On!", frame)

        if cv.waitKey(1) & 0XFF == ord("e"):
            break

video.release()
output.release()
cv.destroyAllWindows()
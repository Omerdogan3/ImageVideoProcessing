import cv2, time

video = cv2.VideoCapture(0)
while True:
    check,frame = video.read()
    print(check)
    print(frame)
    cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #time.sleep(3)
    cv2.imshow("Capturing",frame)
    key = cv2.waitKey(1)

    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()
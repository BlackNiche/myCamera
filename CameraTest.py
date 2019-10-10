import cv2
from datetime import datetime

cam = cv2.VideoCapture(0)  # Sets camera feed number
cam.set(cv2.CAP_PROP_FPS, 60)  # Sets camera settings (FPS)
cam.set(3, 1920)  # Sets x-resolution
cam.set(4, 1080)  # Sets y-resolution
font = cv2.FONT_HERSHEY_PLAIN
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Sets codec ('M', 'J', 'P', 'G') or (*'DIVX')
out = cv2.VideoWriter("output.avi", fourcc, 30, (1280, 720))

while True:
    re, img = cam.read()  # Sets camera read

    img = cv2.flip(img, 1)

    #        (video)        (text)            (Position) (Font)(size)(colour RGB)(font thickness)
    cv2.putText(img, "You are being recorded.", (10, 15), font, 1.2, (1, 1, 1), 1, cv2.LINE_AA)
    cv2.putText(img, str(datetime.now()), (1180, 15), font, 0.5, (1, 1, 1), 1, cv2.LINE_AA)
    cv2.imshow("Recording You... ;)", img)  # Sets the camera program title

    out.write(img)

    key = cv2.waitKey(10) & 0xff
    if key == 27:  # If press 'Esc' then quit
        break

cam.release()
cv2.destroyAllWindows()

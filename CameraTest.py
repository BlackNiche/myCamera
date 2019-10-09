import cv2

cam = cv2.VideoCapture(0) # Sets camera feed number
cam.set(cv2.CAP_PROP_FPS, 60) # Sets camera settings (FPS)
cam.set(3,1920) # Sets x-resolution
cam.set(4,1080) # Sets y-resolution

while True:
    re, img = cam.read() #Sets camera read

    img = cv2.flip(img, 1)

    cv2.imshow("Recording You... ;)", img) #Sets the camera program title
    # out.write(img)

    key = cv2.waitKey(10) & 0xff
    if key == 27: # If press 'Esc' then quit
        break

cam.release()
cv2.destroyAllWindows()
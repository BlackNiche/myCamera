import cv2

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FPS, 10)
cam.set(3,1920)
cam.set(4,1080)
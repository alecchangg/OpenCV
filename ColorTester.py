import cv2
import numpy as np

def empty(x):
    pass

frameWidth = 400
frameHeight = 480

cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)



cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 280)
cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
cv2.createTrackbar("HUE Max", "HSV", 0, 179, empty)
cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT Max", "HSV", 0, 255, empty)
cv2.createTrackbar("VAL Min", "HSV", 0, 255, empty)
cv2.createTrackbar("VAL Max", "HSV", 0, 255, empty)




while True:
    _, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hMin = cv2.getTrackbarPos("HUE Min", "HSV")
    sMin = cv2.getTrackbarPos("SAT Min", "HSV")
    vMin = cv2.getTrackbarPos("VAL Min", "HSV")
    hMax = cv2.getTrackbarPos("HUE Max", "HSV")
    sMax = cv2.getTrackbarPos("SAT Max", "HSV")
    vMax = cv2.getTrackbarPos("VAL Max", "HSV")


    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])
    mask = cv2.inRange(imgHSV, lower, upper)
    result = cv2.bitwise_and(img,img, mask = mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img, result])
    cv2.imshow("Adjust", hStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
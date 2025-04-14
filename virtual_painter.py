import cv2
import numpy as np
import time
import os

from numpy.distutils.conv_template import header

import Handtracking_module as htm

folderpath = "header"
myList = os.listdir(folderpath)
print(myList)

overlaylist = []
for imgpath in myList:
    image = cv2.imread(f"{folderpath}/{imgpath}")
    image = cv2.resize(image, (1280, 90))  # Resize header to match frame width
    overlaylist.append(image)
print(len(overlaylist))

Header = overlaylist[0]

cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Frame width
cap.set(4, 720)   # Frame height

detector = htm.handDetector(detectionCon=0.85)

while True:
    #import image
    success, img = cap.read()
    img = cv2.flip(img,1)

    #hand landmarks
    img = detector.findHands(img)
    lmlist = detector.findPosition(img,draw= False)

    if lmlist and len(lmlist) > 12:
        #print(lmlist)

        #tip of the fingers
        x1,y1 = lmlist[8][1:]
        x2,y2 = lmlist[12][1:]

        #check which fingers are up
        fingers = detector.fingersup()
        print(fingers)

        #selection mode = two fingers
        if fingers[1] and fingers[2]:
            cv2.rectangle(img, (x1,y1-25),(x2,y2 + 25),(255,0,255),cv2.FILLED)
            print("selection mode")
            if y1 < 125:
                if 250 < x1 < 450:
                    header = overlaylist[0]
                elif 550 <x1 <750:
                    header = overlaylist[1]
                elif 800 <x1 <950:
                    header = overlaylist[2]
                elif 1050 <x1 <1200:
                    header = overlaylist[1]

        #drawing mode = one finger
        if fingers[1] and fingers[2] == False:
            cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
            print("drawing mode")






    #setting the header images
    if not success:
        break  # Exit loop if the frame is not captured

    img[0:90, 0:1280] = Header  # Assign resized header to frame

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()

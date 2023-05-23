'''
This code creates for dataset creation. while running u can save sign to each folder that can change in folder and save by clicking "s" and
it show the count of image saved to folders.
'''

import cv2
from cvzone.HandTrackingModule import HandDetector
import time

cap = cv2.VideoCapture(1)
detector = HandDetector(maxHands=2)

counter = 0

folder = "Data/A"


while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    cv2.rectangle(img, (0, 20), (500, 600), (255, 255, 255), 2)

    cv2.imshow("Image", img)
    key= cv2.waitKey(1)
    if key == ord("s"):
       counter += 1
       cv2.imwrite(f"{folder}/Image_{time.time()}.jpg", img)
       print(counter)
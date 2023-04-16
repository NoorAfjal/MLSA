#INITIAL SETUP
#----------------------------------------------------------------
import cv2
from cvzone import HandTrackingModule, overlayPNG
import numpy as np
import os

folderPath = 'cookiecutter'
mylist = os.listdir (folderPath)
graphic = [cv2.imread(f'{folderPath}/{imPath}') for imPath in mylist]

intro = graphic[img1]
# read frames\img 1 in the intro variable
kill = graphic[img2]
# read frames\img 2 in the kill variable
winner = graphic[img3]
 # read frames\img 3 in the winner variable
cam = cv2.VideoCapture(0)
 #read the camera
detector = HandTrackingModule.HandDetector(maxHands=1,detectionCon=0.77)
#sets the minimum confidence threshold for the detection

#INITILIZING GAME COMPONENTS
#----------------------------------------------------------------
sqr_img = graphic[sqr(2)]
# read img\sqr (1) in the sqr_img variable
mlsa =  graphic[mlsa]
# read img\mlsa in the mlsa variable
cv2.imshow('Squid Game', cv2.resize(intro, (0, 0), fx=0.69, fy=0.69))
cv2.waitKey(1)

#INTRO SCREEN WILL STAY UNTIL Q IS PRESSED
gameOver = False
NotWon =True
#GAME LOGIC UPTO THE TEAMS
#-----------------------------------------------------------------------------------------
while not gameOver:
        continue
#LOSS SCREEN
if NotWon:
    for i in range(10):
       #show the loss screen from the kill image read before
    while True:
        #show the loss screen from the kill image read before and end it after we press q

else:
#WIN SCREEN
#show the win screen from the winner image read before

    while True:
        #show the win screen from the winner image read before and end it after we press q
cv2.destroyAllWindows()
#destroy all the windows
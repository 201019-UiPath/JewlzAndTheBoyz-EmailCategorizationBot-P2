import cv2
import os
import win32security
import win32api
import io
import numpy as np


WINDOW_TITLE = "Take photos using SPACE. Close window when done."

def takePhoto( in_IdModulePath, name):
    os.chdir( in_IdModulePath)

    #f = open("teststringimage.txt", "w+")
    cam = cv2.VideoCapture(0)
    cv2.namedWindow(WINDOW_TITLE)
    img_counter = 0
    path = "/train_img/{}/".format(name)

    while cv2.getWindowProperty(WINDOW_TITLE, 0) >= 0:
        ret, frame = cam.read()
        cv2.imshow(WINDOW_TITLE, frame)
        if not ret:
            break
        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "frame_{}.png".format(img_counter)
            cv2.imwrite( in_IdModulePath + path + img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()
    cv2.destroyAllWindows()

    return img_counter

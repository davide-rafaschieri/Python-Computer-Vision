# -*- coding: utf-8 -*-
"""
Created on Fri May 31 19:21:53 2019

@author: David
"""
import cv2
from eyetracker import EyeTracker

camera = cv2.VideoCapture(0)
et = EyeTracker("cascades\\haarcascade_frontalface_default.xml", "cascades\\haarcascade_eye.xml")
while True:
    (grabbed, frame) = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = et.track(gray)
    for rect in rects:
        cv2.rectangle(frame, (rect[0],rect[1]), (rect[2], rect[3]), (0, 255, 0), 2)
    cv2.imshow("Tracking", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
camera.release()
cv2.destroyAllWindows()
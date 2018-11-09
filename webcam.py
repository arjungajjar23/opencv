import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
smile_cascade= cv2.CascadeClassifier("haarcascade_smile.xml")

video_capture = cv2.VideoCapture(0)

while True:

    ret, frame = video_capture.read()
    faces = face_cascade.detectMultiScale(gray, 1.15, 5, (30,30))
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.imshow('Video',frame)
video_capture.release()
cv2.waitKey(0)
cv2.destroyAllWindows()

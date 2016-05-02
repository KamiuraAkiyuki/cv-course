# coding: UTF-8
import cv2
import numpy as np
import glob

face_cascade = cv2.CascadeClassifier('/Users/akiyuki/.pyenv/versions/anaconda3-2.4.1/share/OpenCV/haarcascades/haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('/Users/akiyuki/.pyenv/versions/anaconda3-2.4.1/share/OpenCV/haarcascades/haarcascade_eye.xml')

img = cv2.imread('data/kao3.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
print(faces)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ----------------------------------------------------------- VIDEO INPUT

# capture = cv2.VideoCapture(0)
# if capture.isOpened() is False:
#     raise("IO Error")
#
# while(True):
#     ret, img = capture.read()
#     if not ret:
#         capture.release()
#         print("Cannot capture a frame")
#         break
#
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#     # for (x,y,w,h) in faces:
#     #     img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#     #     roi_gray = gray[y:y+h, x:x+w]
#     #     roi_color = img[y:y+h, x:x+w]
#     #     eyes = eye_cascade.detectMultiScale(roi_gray)
#     #     for (ex,ey,ew,eh) in eyes:
#     #         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

#     # cv2.imshow('image', img)
#     key = cv2.waitKey(1)
#     if key == ord('e'):
#         cv2.destroyAllWindows()
#         break

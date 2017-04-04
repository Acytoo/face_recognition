# Face Recognition learnt form indian
# 2017-04-02 19:20:31

import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
# using your own camera
userId = input('Please enter the user id: ')
sampleNum = 0
while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)
        for (x, y, w, h) in faces:
            cv2.imwrite('dataSet/User.' + str(userId) + '.' + str(sampleNum) + '.jpg',\
                        gray[y:y+h, x:x+w])
            cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
            cv2.waitKey(100)
            sampleNum += 1
            
            
        cv2.imshow('iamge', img)
        k = cv2.waitKey(30) & 0xff
        if sampleNum > 20:
            break

cap.release()
cv2.destroyAllWindows()

                        

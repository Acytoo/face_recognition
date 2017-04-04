# detect the people 
# 2017-04-02 19:20:31

import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
rec = cv2.face.createLBPHFaceRecognizer()
rec.load('recognizer\\trainningData.yml')
Id = 0
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL, 5, 1, 0, 4)

cap = cv2.VideoCapture(0)
# using your own camera


while(True):
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
            Id, conf = rec.predict(gray[y:y+h, x:x+w])
            cv2.cv.PutText(cv2.cv.fromarray(img), str(Id), (x+w, y+h), font, 255)
        cv2.imshow('dectet', img)
        cv2.waitKey(1)
        if(cv2.waitKey(1) == 27):
            break

ccap.release()
cv2.destroyAllWindows()

                        

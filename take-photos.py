# Face Recognition learnt form indian
'''
This part will take photos, so i can train the recognizer later
'''
# 2017-04-02 19:20:31

import cv2
import numpy as np
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# using your own camera
userId = input('Please enter the user id: ')
sampleNum = 0
while True:
        ret, img = cap.read()
        flag = 0
        while ret:
                ret, img = cap.read()
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    cv2.imwrite('dataSet/User.' + str(userId) + '.' + str(sampleNum) + '.jpg',\
                                gray[y:y+h, x:x+w])
                    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
                    cv2.waitKey(100)
                    sampleNum += 1
            
            
                cv2.imshow('iamge', img)
                cv2.waitKey(1)
                if(sampleNum > 40):
                        flag = 1
                        break
        if flag == 1:
                break
                
        

cap.release()
cv2.destroyAllWindows()

                        

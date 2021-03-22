import numpy as np
import cv2

cap  = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalcatface.xml')
print(face_cascade)
while(True):
	ret,frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	
	faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )
	for(x,y,w,h) in faces :
		cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
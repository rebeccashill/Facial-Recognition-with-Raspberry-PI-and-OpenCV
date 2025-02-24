import numpy as np 
import cv2 

#Load cascade file for detecting faces
face_cascade = cv2.CascadeClassifier('/home/pi/opencv
3.1.0/data/haarcascades/haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('/home/pi/opencv
3.1.0/data/haarcascades/haarcascade_eye.xml') 

#Load image from file
img = cv2.imread('sachin.jpg') 

#Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

#Look for faces in the image using the loaded cascade file
faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
print "Found "+str(len(faces))+" face(s)" 

#Draw a rectangle around every found face
for (x,y,w,h) in faces: 
  img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) 
  roi_gray = gray[y:y+h, x:x+w] 
  roi_color = img[y:y+h, x:x+w] 
  
  eyes = eye_cascade.detectMultiScale(roi_gray) 
  for (ex,ey,ew,eh) in eyes: 
    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2) 
  
  #Save the result image
  cv2.imwrite('result1.jpg',img) 
    
  cv2.waitKey(0) 
  cv2.destroyAllWindows()

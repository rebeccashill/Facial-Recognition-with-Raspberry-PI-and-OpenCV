import cv2 

eye_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.1.0/data/haarcascades/ha$ 
face_cascade = cv2.CascadeClassifier('/home/pi/opencv-3.1.0/data/haarcascades/h$ 

img = cv2.imread('sachin.jpg') 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
print "Found "+str(len(faces))+" face(s)" 

#Draw a rectangle around every found face 
for (x,y,w,h) in faces: 
cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) 

#Save the result image 
cv2.imwrite('result1.jpg',img)

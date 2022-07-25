import cv2 

image = cv2.imread('00a87b6bb3.jpg')
x=0
y=5
z=8
h=9
cv2.rectangle(image,(x,y),(x+z,y+h),(0,0,225),3)
cv2.imshow('img',image)
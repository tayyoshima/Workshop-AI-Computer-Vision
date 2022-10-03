import cv2

img = cv2.imread('Image/dog-1920.jpg')
#กำหนดขนาด
img = cv2.resize(img,(500,300)) #(x,y) x คือกว้าง y  คือ สูง

cv2.line(img,(0,0),(400,200),(255,0,0),5 )
cv2.imshow('Output',img)
cv2.waitKey(0)
cv2.destroyAllWindows() #คืนทรัพยากรเครื่อง
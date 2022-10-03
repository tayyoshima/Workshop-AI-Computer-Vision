import cv2

img = cv2.imread('Image/dog-1920.jpg')
imgfinal = cv2.resize(img,(500,300)) #(x,y) x คือกว้าง y  คือ สูง
print(imgfinal)
cv2.imshow('Output',imgfinal)
cv2.waitKey(delay = 0)
#cv2.waitKey(delay = 0) แสดงผลตลอด
#cv2.waitKey(0) แสดงผลตลอด
cv2.destroyAllWindows() #คืนทรัพยากรเครื่อง
import cv2

img = cv2.imread('Image/dog-1920.jpg')

cv2.imshow('Output',img)
cv2.waitKey(delay = 5000)
#cv2.waitKey(delay = 0) แสดงผลตลอด
#cv2.waitKey(0) แสดงผลตลอด
cv2.destroyAllWindows() #คืนทรัพยากรเครื่อง
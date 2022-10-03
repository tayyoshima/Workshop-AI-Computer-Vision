import cv2

img = cv2.imread('Image/dog-1920.jpg',-1)

cv2.imshow('Output',img)
cv2.waitKey(delay = 0)
cv2.destroyAllWindows() #คืนทรัพยากรเครื่อง
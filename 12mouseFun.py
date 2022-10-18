#แสดงพิกัดด้วย Mouse Event
import cv2
img = cv2.imread("Image/dog-1920.jpg")
img = cv2.imread("Image/RGB.png")

#กำหนดขนาดใหม่
img = cv2.resize(img,(500,500)) #(x,y) x คือกว้าง y  คือ สูง

def clickPosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        text = str(x)+","+str(y)
        cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
        cv2.imshow("Output",img)

#แสดงภาพ
cv2.imshow("Output",img)
#ทำงานกับ Mouse
cv2.setMouseCallback("Output",clickPosition)
cv2.waitKey(0)
cv2.destroyAllWindows()
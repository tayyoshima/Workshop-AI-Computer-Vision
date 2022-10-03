import cv2

cap = cv2.VideoCapture('Image/puppy.mp4')

while(cap.isOpened()): #เช็คว่าไฟล์วิดีโอนี้ สามารถเปิดได้จริงหรือไม่
    ret, frame = cap.read() #รับภาพจากกล้อง frame ต่อ frame
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Output',gray)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
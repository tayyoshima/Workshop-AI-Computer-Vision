#https://docs.opencv.org/4.x/dd/d43/tutorial_py_video_display.html
import cv2

cap = cv2.VideoCapture(0)
fourCC = cv2.VideoWriter_fourcc(*'MP4V') #XVID (.avi) MP4V (.mp4)

out = cv2.VideoWriter('Image/outputA.mp4',fourCC,20.0,(640,  480)) #ขนาดเฟรม 640x480 มาตรฐานของกล้อง webcam หากเปลี่ยนขนาด จะบันทึกวิดีโอจากกล้องไม่ได้

while(cap.isOpened()): #เช็คว่าไฟล์วิดีโอนี้ สามารถเปิดได้จริงหรือไม่
    ret, frame = cap.read() #รับภาพจากกล้อง frame ต่อ frame
    if ret == True:
        cv2.imshow('Output',frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()



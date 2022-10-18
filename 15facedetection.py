#https://mybinder.org/v2/gh/xippar/face-dectection-opencv-python/HEAD
#https://medium.com/@wanchatpookhuntod_1602/face-detection-opencv-%E0%B9%84%E0%B8%9E%E0%B8%98%E0%B8%AD%E0%B8%99-%E0%B8%87%E0%B9%88%E0%B8%B2%E0%B8%A2-%E0%B9%86-ef8749f7f473

import cv2

Path_Image = 'Image/face-detection02.jpg'
img = cv2.imread(Path_Image)
detect= cv2.CascadeClassifier("face_detection/haarcascade_frontalface_default.xml")
face = detect.detectMultiScale(img)
#ได้ตำแหน่งของใบหน้ามา
print(face)
#กรณีมีใบหน้าเดียว
#x, y, w, h = face[0]
#cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255), 2)


for x,y,w,h in face: # ค่า x คือตำแหน่งแนวนอนของใบหน้า, y คือคือตำแหน่งแนวตั้งของใบหน้า , w คือค่าความกว้างใบหน้า h ค่าความสูงใบหน้า
    #ใช้คำสั่ง cv2.rectangle() ที่รับค่า 
    #ภาพที่ต้องการตีกรอบ, tuple จุดเริ่มต้นที่จุดซ้ายบน (x,y), tuple จุดสิ้นสุดที่จุดขวาล่าง หรือ (x+w,y+h), tuple ค่าสี BGR สีเขียวใช้ (0,255,0), และความหนาของกรอบที่ต้องการ
    cv2.rectangle(img, (x,y),(x+w,y+h),(0,0,255), 2)

    
cv2.imshow('out_put', img)
cv2.waitKey()
cv2.destroyAllWindows()
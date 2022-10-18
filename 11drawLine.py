import cv2

img = cv2.imread('Image/dog-1920.jpg')
#กำหนดขนาด
img = cv2.resize(img,(500,300)) #(x,y) x คือกว้าง y  คือ สูง

cv2.line(img,(0,0),(500,300),(255,0,0),5 )
cv2.arrowedLine(img,(150,150),(300, 150),(0,0,255),5 )
cv2.rectangle(img,(0,0),(300, 300),(0,255,0),5 )
cv2.circle(img,(250,250),30,(0,255,0),5 ) #รูปภาพ, ตำแหน่งจุดศูนย์กลาง (x,y) , รัศมี, สี , ความหนา (หากใส่ - 1 จะได้วงกลมสีทึบ)

# putText(ภาพ,ข้อความ,พิกัดที่จะแสดงข้อความ (x,y),font,ขนาดข้อความ,สี,ความหนา)
cv2.putText(img,"ARIT",(100,100),cv2.FONT_HERSHEY_SIMPLEX,1.8,(0,0,255),2)


cv2.imshow('Output',img)
cv2.waitKey(0)
cv2.destroyAllWindows() #คืนทรัพยากรเครื่อง

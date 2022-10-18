import cv2 
import numpy

while True :
    img=cv2.imread("Image/fruit.png")
    #img=cv2.resize(img,(400,400))

    #ช่วงของสี BGR
    lower = numpy.array([157,42,89]) #ช่วงสีที่เข้มที่สุด
    upper = numpy.array([173,126,184]) #ช่วงสีที่จางที่สุด

    mask=cv2.inRange(img,lower,upper)
    result = cv2.bitwise_and(img,img,mask=mask)
    if cv2.waitKey(0) & 0xFF == ord("e"):
        break

    cv2.imshow("Original",img)
    cv2.imshow("Mask",mask)
    cv2.imshow("Result",result)
    cv2.imwrite('Image/outputA.jpg',img)
    cv2.imwrite('Image/outputB.jpg',mask)
    cv2.imwrite('Image/outputC.jpg',result)


cv2.destroyAllWindows()
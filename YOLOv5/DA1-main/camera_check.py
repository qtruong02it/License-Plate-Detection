import pymongo 
import cv2
import pyqrcode
from ocr import getStr

cam = cv2.VideoCapture(1)
cam.set(3,640)
cam.set(4,480)

while True:
    ret, frame = cam.read()
    if not ret:
        break
    cv2.imshow("popBike", frame)
    k = cv2.waitKey(1)
    #if k%256 == 27:
        # ESC pressed
        #break
    if k%256 == 32:
        # SPACE pressed
        img_name = "Bike.png"
        cv2.imwrite(img_name, frame)
        #cv2.imshow("pic", frame);
        break
        #print("{} written!".format(img_name))
        #print("cho xe vao")
        #img_counter += 1
cam.release()
cv2.destroyAllWindows()



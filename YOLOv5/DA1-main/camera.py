import cv2
#set window size (640 x 480)
cam = cv2.VideoCapture(1)
cam.set(3,640)
cam.set(4,480)
# display the camera
# press SPACE to take a shot
while True:
    ret, frame = cam.read()
    if not ret:
        break
    cv2.imshow("getBike", frame)
    k = cv2.waitKey(1)
    if k%256 == 32:
        # SPACE pressed
        img_name = "Bike.png"
        cv2.imwrite(img_name, frame)
        break
cam.release()
cv2.destroyAllWindows()

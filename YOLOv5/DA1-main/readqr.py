import cv2 #Read image / camera/video input
import os
from pyzbar.pyzbar import decode
import time
from ocr import getStr
from OCR_reg import character_segmentation
import pymongo
import bson

# -------------------------------------recut------------------------------------------
# img = cv2.imread("test.jpg", 0)
# a = character_segmentation(debug=True)
# UpStrg, DownStrg = a.no_segment(img)
# print(UpStrg, DownStrg)
# cv2.waitKey(0)
# -------------------------------------recut------------------------------------------

# ----------------------------------no recut------------------------------------------
#recognize the text
path = 'runs/detect/exp/crops/bienso/Bike.jpg'
UpStrg, DownStrg = getStr(path)
#double check OCR
print("BIEN SO DOC DUOC LA: ", UpStrg, " - ", DownStrg)
print("Neu SAI, an 0")
print("Neu DUNG, an 1")
key = input()
if (key == '0'):
    os.system('python popBike.py')
elif(key == '1'):
# ----------------------------------no recut------------------------------------------
#call camera for read QR code
    cap = cv2. VideoCapture (1)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("QR", frame)
        k = cv2.waitKey(1)
        if (decode(frame) != []):
            for code in decode (frame):
                qr_dectect = code.data.decode ('utf-8')
            break
    cap.release()
    cv2.destroyAllWindows()
    '''
    camera = True
    while camera == True:
        success, frame = cap.read ()
        for code in decode (frame):
            qr_dectect = code.data.decode ('utf-8')
            camera = False
    '''

    id = bson.objectid.ObjectId(qr_dectect)

#access to database
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client["License_Plate_Manager"]
    information = db.table0
#veryfy ORcode and text on the plate
    result = information.find({'_id' : id})
    apr = 0
    rs=information.find({"_id":{"$exists":True}})
    cnt = information.count_documents({})
    for index in range (0 , cnt): 
        if (rs[index]["_id"] == id):
            apr = 1
    acp = 0
    if(apr == 1 ):
        for res in result:
            if(res["Taken"]==False):
                if UpStrg == res["Up"] and DownStrg == res["Down"]:
                    acp = 1
                else:
                    acp = 0
            else:
                print("XE DA DUOC LAY THANH CONG")

        if (acp == 1): 
            print("LAY XE THANH CONG")
            db.table0.update_one({"_id": id},{ "$set": { 'Taken': True } })
        
    else:
        print("SAI QR, thu lai")
        os.system('python readqr.py')







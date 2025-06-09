import cv2 #Read image / camera/video input
from pyzbar.pyzbar import decode
import time
from ocr import getStr
from OCR_reg import character_segmentation
import pymongo
import bson
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

id = bson.objectid.ObjectId(qr_dectect)

client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client["License_Plate_Manager"]
information = db.table0

result = information.find({'_id' : id})
rs=information.find({"_id":{"$exists":True}})
cnt = information.count_documents({})
apr = 0
for index in range (0 , cnt): 
    if (rs[index]["_id"] == id):
        apr = 1
print(apr)
#rs=information.find({"_id":{"$exists":True}})


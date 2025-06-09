import pymongo
import pyqrcode
import time
import cv2
import os
from ocr import getStr
from PIL import ImageDraw
from PIL import Image, ImageFont
from OCR_reg import character_segmentation

#access to database
client = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = client['License_Plate_Manager']
information = mydb.table0

# -------------------------------------recut------------------------------------------
# img = cv2.imread("test.jpg", 0)
# a = character_segmentation(debug=True)
# UpStrg, DownStrg = a.no_segment(img)
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
    os.system('python getBike.py')
elif(key == '1'):
# ----------------------------------no recut------------------------------------------

# init string on QRcode image
    #sec = current time
    sec = time.localtime()
    curtime_date = ''
    curtime_hour = ''
    for item in sec[0:3]:
        curtime_date = curtime_date + str(item) + "/"

    for item in sec[3:6]:
        curtime_hour = curtime_hour + str(item) + ":"
        
    new_str_date = curtime_date.rstrip ("/")
    new_str_hour = curtime_hour.rstrip (":")
#import data to database
    rec= [{
        "time" : sec,
        "Up" : UpStrg,
        "Down": DownStrg,
        "Taken": False
        }]
    information.insert_many(rec)

    id = information.find({'time' : sec})
    for i in id:
        input_data =str(i["_id"])

#generate QR code and add some information string
    qr = pyqrcode.create(input_data)
    qr.png("QR.png", scale = 8)

    image = Image.open('QR.png')
    width, height = image.size
    draw = ImageDraw.Draw(image)
    Up = UpStrg
    Down = DownStrg
    font = ImageFont.load_default()
    draw.text((40, 5), str(new_str_date), font=font)
    draw.text((210, 5), str(new_str_hour), font=font)
    draw.text((40,height - 20), Up, font=font)
    draw.text((40,height - 10), Down, font=font)
    image.save("QRnew.png")
    #popup the QR code
    Img=Image.open('QRnew.png')
    Img.show()
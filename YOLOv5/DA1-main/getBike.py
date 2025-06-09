import os
import shutil
import cv2
from OCR_reg import character_segmentation

# --------------------------------remove path------------------------------
remove_path = "runs"
crop_path = "runs/detect/exp/crops"
if os.path.exists(remove_path):
        shutil.rmtree(remove_path)
QR_path = "QR.png"
if os.path.exists(QR_path):
        os.remove(QR_path)

QR_new_path = "QRnew.png"
if os.path.exists(QR_new_path):
        os.remove(QR_new_path)

ts_path = "test.jpg"
if os.path.exists(ts_path):
        os.remove(ts_path)

# -------------------------------------recut------------------------------------------
# flag = 0
# while ((os.path.exists(crop_path) == False) | (flag == 0)):               # if fail to frist cut or recut then try again to sucess
#         if os.path.exists(remove_path):
#             shutil.rmtree(remove_path)
#         os.system('python camera.py')                                     # call camera
#         os.system('python detect.py --source Bike.png --save-crop')       # detect plate then first cut (no sharp)
#         if (os.path.exists(crop_path)):
#             os.system('python re_cut.py')                                 # recut to be sharper
#             img = cv2.imread("test.jpg", 0)                               # check if the cut is done ~ flag = 1
#             a = character_segmentation(debug=True)                        # if not ~ flag = 0
#             lenght = a.getLen(img)
#             if(lenght != 0):
#                 flag = 1
# os.system('python import_data.py')                                        # import plate number and necessary data to database

# -------------------------------------recut------------------------------------------

# ----------------------------------no recut------------------------------------------
while (os.path.exists(crop_path) == False):
    os.system('python camera.py')                                    # call camera
    os.system('python detect.py --source Bike.png --save-crop')      # detect plate then cut (no sharp)
    os.system('python import_data.py')                               # import plate number and necessary data to database

# ----------------------------------no recut------------------------------------------
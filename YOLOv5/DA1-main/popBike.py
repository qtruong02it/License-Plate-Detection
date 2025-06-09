import os 
import shutil
import cv2
from OCR_reg import character_segmentation

# ----------------------------------remove path--------------------------------------
crop_path = "runs/detect/exp/crops"
remove_path = "runs"
ts_path = "test.jpg"
if os.path.exists(ts_path):
        os.remove(ts_path)
if os.path.exists(remove_path):
    shutil.rmtree(remove_path)

# -------------------------------------recut------------------------------------------
# flag = 0
# while ((os.path.exists(crop_path) == False) | (flag == 0)):               # if fail to frist cut or recut then try again to sucess
#         if os.path.exists(remove_path):
#             shutil.rmtree(remove_path)
#         os.system('python camera_check.py')                               # call camera
#         os.system('python detect.py --source Bike.png --save-crop')       # detect plate then first cut (no sharp)
#         if (os.path.exists(crop_path)):
#             os.system('python re_cut.py')                                 # recut to be sharper
#             img = cv2.imread("test.jpg", 0)                               
#             a = character_segmentation(debug=True)                        # recognize the text on plate
#             lenght = a.getLen(img)
#             if(lenght != 0):                                              # check if the cut is done ~ flag = 1
#                 flag = 1                                                  # if not ~ flag = 0
# os.system('python readqr.py')                                             # call camera to check QRcode then compare with database

# -------------------------------------recut------------------------------------------

# ----------------------------------no recut------------------------------------------
while (os.path.exists(crop_path) == False):
    if os.path.exists(remove_path):
        shutil.rmtree(remove_path)
    os.system('python camera_check.py')                              # call camera
    os.system('python detect.py --source Bike.png --save-crop')      # detect plate then cut (no sharp)
os.system('python readqr.py')                                        # call camera to check QRcode then compare with database

# ----------------------------------no recut------------------------------------------

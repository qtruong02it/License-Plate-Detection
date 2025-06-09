import cv2
from OCR_reg import character_segmentation

img = cv2.imread("test.jpg", 0)
a = character_segmentation(debug=True)
r = a.no_segment(img)
cv2.waitKey(0)
print(r)
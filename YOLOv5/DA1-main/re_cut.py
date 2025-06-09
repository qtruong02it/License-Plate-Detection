import cv2 
import numpy as np

img = cv2.imread('runs/detect/exp/crops/bienso/Bike.jpg', 0)
height, width = img.shape
new_width = 200
new_height = int(img.shape[0] * 200 / width) # keep original height
dim = (new_width, new_height)

# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

#cv2.imshow('Resized', resized)
ret, thresh = cv2.threshold(resized, 80, 255, cv2.THRESH_BINARY)
#cv2.imshow('Threshold', thresh)
blur = cv2.GaussianBlur(thresh, (5, 5), 0)
im_bw = cv2.Canny(thresh, 10, 200)
#cv2.imshow('Im_bw', im_bw)
contours, _ = cv2.findContours(im_bw, cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)

contours = sorted(contours, key=cv2.contourArea, reverse=True)[:1]
# print(contours)
cnts = cv2.drawContours(resized.copy(), contours, -1, (0, 255, 0), 3)

#cv2.imshow('cnts', cnts)
min_x, min_y = new_width, new_height
max_x = max_y = 0

for i in contours:
    rect = cv2.minAreaRect(i)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    # cv2.drawContours(img, [box], -1, (0, 255, 0), 2)
    # cv2.imshow("Output", img)

    # cat anh de doc chu
    W = rect[1][0]
    H = rect[1][1]

    Xs = [i[0] for i in box]
    Ys = [i[1] for i in box]
    x1 = min(Xs)
    x2 = max(Xs)
    y1 = min(Ys)
    y2 = max(Ys)

    angle = rect[2]
    if angle > 45:
        angle -= 90

    # xoay ảnh
    center = ((x1 + x2) / 2, (y1 + y2) / 2)
    # Size of the upright rectangle bounding the rotated rectangle
    size = (x2 - x1, y2 - y1)
    M = cv2.getRotationMatrix2D((size[0] / 2, size[1] / 2), angle, 1.0)
    # Cropped upright rectangle
    cropped = cv2.getRectSubPix(resized, size, center)
    cropped = cv2.warpAffine(cropped, M, size)
    croppedW = H if H > W else W
    croppedH = H if H < W else W
    # Final cropped & rotated rectangle
    ROI = cv2.getRectSubPix(cropped, (int(croppedW), int(croppedH)), (size[0] / 2, size[1] / 2))
    #cv2.imshow('ROI', ROI)
    cv2.imwrite('./test.jpg', ROI)
cv2.waitKey(0)
import cv2 as cv
import numpy as np
import math

img = cv.imread("../erp.png")
W = 1920
H = 960
cx = W/2
cy = H/2
hfov = 120
vfov = 90
PI = math.pi
f = W / (2 * PI)
Wd = int(2*f*math.tan(math.radians(hfov/2)))
Hd = int(2*f*math.tan(math.radians(vfov/2)))
dcx = Wd/2
dcy = Hd/2
dst = []
for y in range(0,Hd) :
    dst_y = []
    for x in range(0,Wd) :
        dst_x = [0,0,0]
        dst_y.append(dst_x)
    dst.append(dst_y)
dst = np.array(dst,dtype=np.uint8)

cv.namedWindow('windw')

for x in range(0,Wd-1):
    for y in range(0,Hd-1):
        D = math.sqrt((x-dcx)**2+(y-dcy)**2)
        if D == 0 :
            continue
        img_x = math.asin((x-dcx)/D)*W/(2*PI)+cx
        pi = math.atan(f/D) 
        img_y= pi *H/PI +cy
        dst[y,x] = img[int(img_y),int(img_x)]
cv.imshow('windw',dst)

cv.waitKey()

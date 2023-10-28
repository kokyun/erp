import cv2 as cv
import numpy as np
import math

img = cv.imread("../erp.png")

W = 1920
H = 960
cx = W/2
cy = H/2
hfov = 160
vfov = 50
PI = math.pi
f = W / (2 * PI)
Wd = int(2*f*math.tan(math.radians(hfov/2)))
Hd = int(2*f*math.tan(math.radians(vfov/2)))
print(Wd ,Hd)
dcx = Wd/2
dcy = Hd/2
theta = math.radians(90)
dst = []
for y in range(0,abs(Hd)) :
    dst_y = []
    for x in range(0,abs(Wd)) :
        dst_x = [0,0,0]
        dst_y.append(dst_x)
    dst.append(dst_y)
dst = np.array(dst,dtype=np.uint8)
cv.namedWindow('windw')

for x in range(0,abs(Wd)-1):
    xth = math.atan((x-dcx)/f)
    img_x = (xth+theta)*W / PI 
    yf = f / np.cos(xth)
    for y in range(0,abs(Hd)-1):
        yth = math.atan((y-dcy)/yf)
        img_y = yth * H / PI + H/2
        dst[y,x] = img[int(img_y),int(img_x)]
cv.imshow('windw',dst)
cv.waitKey()

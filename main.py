import numpy as np
import cv2 as cv
def nothing(x):
    pass
# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
height, width = img.shape[:2]
cv.namedWindow('image')
# create trackbars for color change
cv.createTrackbar('R','image',0,255,nothing)
cv.createTrackbar('G','image',0,255,nothing)
cv.createTrackbar('B','image',0,255,nothing)
cv.createTrackbar('Figure', 'image',0,2,nothing)
cv.createTrackbar('Size', 'image',0,width,nothing)

while(1):
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    # get current positions of four trackbars
    r = cv.getTrackbarPos('R','image')
    g = cv.getTrackbarPos('G','image')
    b = cv.getTrackbarPos('B','image')
    f = cv.getTrackbarPos('Figure', 'image')
    s = cv.getTrackbarPos('Size', 'image')
    img[:] = [b,g,r]
    if f == 1 and s != 0:
        cv.rectangle(img,(width//2-s//2,height//2-s//2),(width//2+s//2,height//2 + s//2),(0,255,0),3)
    elif f == 2 and s != 0:
        cv.circle(img,(width//2,height//2), s, (0,255,0), -1)
cv.destroyAllWindows()
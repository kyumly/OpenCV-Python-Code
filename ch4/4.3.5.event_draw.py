import numpy as np
import cv2

orange, blue, white = (0, 165, 255), (255, 0, 0), (255,255,255) # 색상 지정
image = np.full((300, 700, 3), white, np.uint8)
title = 'test'
pt = (-1, -1)

def onMouse(event, x, y, flags, param):
    global pt

    if event == cv2.EVENT_LBUTTONDOWN:
        if pt[0] < 0 :
            pt = (x, y)
        else:
            cv2.rectangle(image, pt, (x,y), blue, 2)
            cv2.imshow(title,image)
            pt = (-1, -1)




cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()



import numpy as np
import cv2



def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("왼쪽  버튼 클릭")

img = np.full((200, 300), 255, np.uint8)


title1,title2 = "m1", "m2"

cv2.imshow("m1", img)
cv2.imshow("m2", img)


cv2.setMouseCallback(title1, onMouse)

cv2.waitKey(0)
cv2.destroyAllWindows()
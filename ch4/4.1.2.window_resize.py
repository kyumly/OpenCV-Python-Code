import numpy as np
import cv2

image = np.zeros((200, 300), np.uint8)
image.fill(255)

t1, t2 = "AUTO", "NORMAL"

cv2.namedWindow(t1, cv2.WINDOW_AUTOSIZE)
cv2.namedWindow(t2, cv2.WINDOW_NORMAL)


cv2.imshow(t1, image)
cv2.imshow(t2, image)
cv2.resizeWindow(t1, 400, 300)
cv2.resizeWindow(t2, 400, 300)


cv2.waitKey(0)
cv2.destroyAllWindows()


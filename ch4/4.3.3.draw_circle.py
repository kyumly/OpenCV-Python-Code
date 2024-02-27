import numpy as np
import cv2

blue, green, red = (255, 0, 0), (0, 255, 0), (0,0,255)
white, black = (255, 255, 255), (0,0,0)
image = np.full((300, 500,3),white, np.uint8)


w, h, _ = image.shape
w_half = int(w // 2)
h_half = int(h // 2)

pt1, pt2 = (300, 50), (100, 220) # 문자열 위치 좌표
shade = (pt2[0] + 2, pt2[1] + 2) # 그림자 좌표
center = (h_half, w_half)

cv2.circle(image, center, 100, blue)
cv2.circle(image, pt1, 50, green, 2)
cv2.circle(image, pt2, 70, red, -1)

font = cv2.FONT_HERSHEY_COMPLEX

cv2.putText(image, "center_blue", center, font, 1.0, blue)
cv2.putText(image, "pt1_green", pt1, font, 0.8, green)
cv2.putText(image, "pt2_red", shade, font, 1.2, black, 2)
cv2.putText(image, "pt2_red2", pt2, font, 1.2, red, 1)


cv2.imshow("test", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
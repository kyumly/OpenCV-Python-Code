import numpy as np
import cv2
from matplotlib import pyplot as plt


orange, blue, white = (0, 165, 255), (255, 0, 0), (255,255,255) # 색상 지정
image = np.full((300, 700, 3), white, np.uint8)

pt1, pt2 = (180, 150), (550, 150)                       # 타원 중심점
size = (120, 60)                                        # 타원 크기 - 반지름 값임


cv2.circle(image, pt1, 1, 0, 2)                         # 타원의 중심점(2화소 원) 표시
cv2.circle(image, pt2, 1, 0, 2)

cv2.ellipse(image, pt1, size,  0, 0, 360, blue, 1)      # 타원 그리기
cv2.ellipse(image, pt2, size, 90, 0, 360, blue, 1)
cv2.ellipse(image, pt1, size,  0, 30, 270, orange, 4)   # 호 그리기
cv2.ellipse(image, pt2, size, 90, 0,  90, orange, 4)

cv2.imshow('test', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
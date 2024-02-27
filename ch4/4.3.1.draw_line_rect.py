import numpy as np
import cv2
from matplotlib import pyplot as plt

blue, green, red = (255, 0, 0), (0, 255, 0), (0,0,255)
image = np.zeros((400, 600,3), np.uint8)
image[:] = (255, 255, 255) # 3채널 흰색

pt1, pt2 = (0, 0), (250, 150)
pt3, pt4 = (400, 150), (500, 50)
roi = (50, 200, 200, 100) # 시갹형 영역 = 4원소 튜플


cv2.line(image, pt1, pt2, red)
cv2.line(image, pt3, pt4, cv2.LINE_AA)

# 사각형 그리기
print(cv2.rectangle(image, pt1, pt2, blue, 3, cv2.LINE_4).shape)
cv2.rectangle(image, roi, red, 3 , cv2.LINE_8)
cv2.rectangle(image, (400,200,100,100), green, cv2.FILLED)

cv2.imshow("test", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# img3 = image.copy()
# cv2.line(image, pt1, pt2, red)
# cv2.line(image, pt3, pt4, green, 3, cv2.LINE_AA) # 계산 현상 감소선
# print(img3[0])
# print(image[0])
# b, g, r = cv2.split(image)
# image2 = cv2.merge([r, g, b])
#
# cv2.rectangle(image, pt1, pt2, blue, 3, cv2.LINE_4) # 4방향 연결선
# cv2.rectangle(image, roi, red, 3, cv2.LINE_8) # 8방향 연결선
# cv2.rectangle(image, (400, 200, 100, 100), green, cv2.FILLED) # 내부채움
# b, g, r = cv2.split(image)
# image2 = cv2.merge([r, g, b])
#
# plt.imshow(image2)
# plt.xticks([])  # x축 눈금
# plt.yticks([])  # y축 눈금
# plt.show()
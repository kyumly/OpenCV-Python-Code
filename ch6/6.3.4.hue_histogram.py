import cv2
import matplotlib.pyplot as plt
#1 이미지 로딩하기

image = cv2.imread('img/hue_hist.jpg', cv2.IMREAD_COLOR)
cv2.imshow("color image", image)


channels = cv2.split(image)

colors = ("b", "g", "r")
hist_list = []



for color, channel in zip(colors, channels):
    hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
    plt.plot(hist, color = color)
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()



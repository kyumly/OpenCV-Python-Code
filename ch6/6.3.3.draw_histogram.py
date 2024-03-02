import cv2
import numpy as np
import matplotlib.pylab as plt

def drwa_histo(hist, shape=(200,256)):
    hist_img = np.full(shape, 255, np.uint8)
    print(hist[0])
    #cv2.normalize(hist, hist,0 , shape[0], cv2.NORM_MINMAX)
    print(hist[0])

    grap = hist_img.shape[1]/ hist.shape[0]
    print(grap)

    for i,h in enumerate(hist):
        x = int(round(i * grap))
        w = int(round(grap))
        cv2.rectangle(hist_img, (x,0,w,int(h)), 0, cv2.FILLED)
    return cv2.flip(hist_img, 0)

image = cv2.imread('img/pixel.jpg', cv2.IMREAD_GRAYSCALE)
if image is None :
    raise Exception("영상파일 읽기 오류")

hist = cv2.calcHist([image], [0], None, [32], [0, 256])
plt.plot(hist)
plt.show()

hist_img = drwa_histo(hist)

cv2.imshow("image", image)
cv2.imshow("hist_img", hist_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
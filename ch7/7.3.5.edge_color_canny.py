import cv2

def onTrackBar(th):
    rep_edge = cv2.GaussianBlur(th, (5, 5), 0)
    rep_edge = cv2.Canny(rep_edge, th, th*2, 5)
    h,w = image.shpe
    cv2.rectangle(rep_edge, (0,0,w,h), 255, -1)
    color_edge =cv2.bitwise_and(rep_edge, rep_image, mask=rep_edge)
    cv2.imshow('Edge', color_edge)


image = cv2.imread('img/edge.jpg', cv2.IMREAD_GRAYSCALE)
th=50

rep_image = cv2.repeat(image, 1, 2)
rep_gray = cv2.cvtColor(rep_image, cv2.COLOR_RGB2GRAY)
cv2.namedWindow('Edge', cv2.WINDOW_NORMAL)
cv2.createTrackbar('Channy th', "color edge", th,100, onTrackBar)
onTrackBar(th)

cv2.waitKey(0)

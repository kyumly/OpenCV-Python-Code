import numpy as np
import cv2

title = 'trackbar'

image = np.zeros((300, 500), np.uint8)

def onChange(value):
    print(value)
    add_value = value - int(image[0][0])
    print("추가 화소 : ", add_value)
    image[:] = add_value + image
    cv2.imshow(title, image)






cv2.imshow(title, image)

cv2.createTrackbar('test', title, image[0][0], 255, onChange)
cv2.waitKey(0)
cv2.destroyAllWindows()

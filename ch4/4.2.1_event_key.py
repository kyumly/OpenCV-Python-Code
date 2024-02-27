import numpy as np
import cv2
switch_case = {
    ord('a') : 'a key input',
    ord('b') : "b키 입력",
    int('0x42', 16) : "8키 입력",
    2424832 : "왼쪽키 입력",
    2490368 : "윗쪽키 입력",
    2555904 : "오른쪽 입력",
    2621440 : "아래쪽 입력"
}

image = np.zeros((200, 300), np.float32)

cv2.namedWindow('Keyboard event')
cv2.imshow('Keyboard event', image)


while True:
    key = cv2.waitKeyEx(100)

    if key == 27 :
        break
    try:
        result = switch_case[key]
        print(result)
    except KeyError:
        result = -1
cv2.destroyAllWindows()


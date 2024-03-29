import cv2
import numpy as np
import time

def scaling(image, size):
    dst = np.zeros(size[::-1], image.dtype)
    #ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    ratioY, ratioX = size[1] / image.shape[0],size[0]/image.shape[1]
    print(ratioY, ratioX)
    y = np.arange(0, image.shape[0], 1)
    x = np.arange(0, image.shape[1], 1)
    y, x = np.meshgrid(y, x)
    print(y)
    i, j = np.int32(y * ratioY), np.int32(x * ratioX)
    print(i)
    dst[i, j] = image[y, x]
    return dst

def scaling2(img, size):  # 크기 변경 함수
    dst = np.zeros(size[::-1], img.dtype)  # 행렬과 크기는 원소가 역순
    ratioY, ratioX = np.divide(size[::-1], img.shape[:2])
    for y in range(img.shape[0]):  # 입력 영상 순회 - 순방향 사상
        for x in range(img.shape[1]):
            i, j = int(y * ratioY), int(x * ratioX)  # 목적 영상의 y, x 좌표
            dst[i, j] = img[y, x]
    return dst

def time_check(func, image, size, title):  ## 수행시간 체크 함수
    start_time = time.perf_counter()
    ret_img = func(image, size)
    elapsed = (time.perf_counter() - start_time) * 1000
    print(title, " 수행시간 = %0.2f ms" % elapsed)
    return ret_img


if __name__ == '__main__':
    image = cv2.imread("./img/scaling.jpg", cv2.IMREAD_GRAYSCALE)
    dst1 = scaling(image, (150, 200))  # 크기 변경 - 축소
    dst2 = scaling2(image, (150, 200))  # 크기 변경 - 축소
    dst3 = time_check(scaling, image, (300, 400), "[방법1] 정방행렬 방식>")
    dst4 = time_check(scaling2, image, (300, 400), "[방법2] 반복문 방식>")

    cv2.imshow("image", image)
    cv2.imshow("dst1- zoom out", dst1)
    cv2.imshow("dst3- zoom out", dst3)
    cv2.resizeWindow("dst1- zoom out", 260, 200)  # 윈도우 크기 확장
    cv2.waitKey(0)
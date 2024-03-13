import cv2
import numpy as np


def filter(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)                     # 회선 결과 저장 행렬
    xcenter, ycenter = mask.shape[1]//2, mask.shape[0]//2       # 마스크 중심 좌표

    for i in range(ycenter, rows - ycenter):                    # 입력 행렬 반복 순회
        for j in range(xcenter, cols - xcenter):
            y1, y2 = i - ycenter, i + ycenter + 1               # 관심영역 높이 범위
            x1, x2 = j - xcenter, j + xcenter + 1               # 관심영역 너비 범위
            roi = image[y1:y2, x1:x2].astype("float32")         # 관심영역 형변환

            tmp = cv2.multiply(roi, mask)                       # 회선 적용 - OpenCV 곱셈
            dst[i, j] = cv2.sumElems(tmp)[0]                    # 출력화소 저장
    return dst



def differential(image, data1, data2):
    mask1 = np.array(data1, np.float32).reshape(3, 3)
    mask2 = np.array(data2, np.float32).reshape(3, 3)

    dst1 = filter(image, mask1)                     # 사용자 정의 회선 함수
    dst2 = filter(image, mask2)
    dst = cv2.magnitude(dst1, dst2)                 # 회선 결과 두 행렬의 크기 계산

    dst = cv2.convertScaleAbs(dst)                      # 윈도우 표시 위해 OpenCV 함수로 형변환 및 saturation 수행
    dst1 = cv2.convertScaleAbs(dst1)
    dst2 = cv2.convertScaleAbs(dst2)
    return dst, dst1, dst2



if __name__ == '__main__':
    image = cv2.imread("img/edge.jpg", cv2.IMREAD_GRAYSCALE)
    if image is None: raise Exception("영상파일 읽기 오류")

    data1 = [-1, 0, 1,  # 프리윗 수직 마스크
             -1, 0, 1,
             -1, 0, 1]
    data2 = [-1, -1, -1,  # 프리윗 수평 마스크
             0, 0, 0,
             1, 1, 1]
    dst, dst1, dst2 = differential(image, data1, data2)

    cv2.imshow("image", image)
    cv2.imshow("prewitt edge", dst)
    cv2.imshow("dst1 - vertical mask", dst1)
    cv2.imshow("dst2 - horizontal mask", dst2)
    cv2.waitKey(0)
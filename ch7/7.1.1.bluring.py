import cv2
import numpy as np
import cv2 as cv

def filter(image, mask):
    rows, cols = image.shape
    dst = np.zeros((rows, cols), np.float32)
    y_center, x_center = rows//2, cols//2

    m_x, m_y = mask.shape
    m_x_center,m_y_center =m_x//2, m_y//2

    for i in range(m_x_center, rows - m_x_center):
        x1, x2 = i - m_x_center, i + m_x_center + 1

        for j in range(m_y_center, cols - m_y_center):
            y1, y2 = j - m_y_center, j + m_y_center + 1
            roi = image[x1:x2, y1:y2].astype(np.float32)
            tmp = roi * mask
            dst[i, j] = cv2.sumElems(tmp)[0]

    return dst

def filter2(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)                 # 회선 결과 저장 행렬
    xcenter, ycenter = mask.shape[1]//2, mask.shape[0]//2  # 마스크 중심 좌표

    for i in range(ycenter, rows - ycenter):                  # 입력 행렬 반복 순회
        for j in range(xcenter, cols - xcenter):
            sum = 0.0
            for u in range(mask.shape[0]):                    # 마스크 원소 순회
                for v in range(mask.shape[1]):
                    y, x = i + u - ycenter , j + v - xcenter
                    sum += image[y, x] * mask[u, v]           # 회선 수식
            dst[i, j] = sum
    return dst


if __name__ == "__main__":
    data = cv.imread("img/filter_blur.jpg", cv.IMREAD_GRAYSCALE)
    if data is None:
        raise Exception("파일 없음")

    mask = np.zeros((3,3), dtype=np.float32)
    mask[:] = 1/9
    blur1 = filter(data, mask)  # 회선 수행 - 화소 직접 접근
    blur2 = filter2(data, mask)  # 회선 수행
    cv2.imshow("image", data)
    cv2.imshow("blur1", blur1.astype("uint8"))
    cv2.imshow("blur2", cv2.convertScaleAbs(blur1))
    cv2.waitKey(0)

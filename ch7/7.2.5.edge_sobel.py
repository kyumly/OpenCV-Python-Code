import numpy as np, cv2
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
    # 입력 인자로 마스크 행렬 초기화
    mask1 = np.array(data1, np.float32).reshape(3, 3)
    mask2 = np.array(data2, np.float32).reshape(3, 3)

    # 사용자 정의 회선 함수
    dst1 = filter(image, mask1)
    dst2 = filter(image, mask2)
    dst = cv2.magnitude(dst1, dst2);  # 회선 결과 두 행렬의 크기 계산

    # dst1, dst2 = np.abs(dst1), np.abs(dst2)  # 회선 결과 행렬 양수 변경
    dst = cv2.convertScaleAbs(dst)
    dst1 = cv2.convertScaleAbs(dst1)
    dst2 = cv2.convertScaleAbs(dst2)
    return dst, dst1, dst2

if __name__ == '__main__':

    image = cv2.imread("img/edge.jpg", cv2.IMREAD_GRAYSCALE)
    if image is None: raise Exception("영상파일 읽기 오류")

    data1 = [-1, 0, 1,  # 수직 마스크
             -2, 0, 2,
             -1, 0, 1]
    data2 = [-1, -2, -1,  # 수평 마스크
             0, 0, 0,
             1, 2, 1]
    dst, dst1, dst2 = differential(image, data1, data2)  # 두 방향 회선 및 크기(에지 강도) 계산

    # OpenCV 제공 소벨 에지 계산
    dst3 = cv2.Sobel(np.float32(image), cv2.CV_32F, 1, 0, 3)  # x방향 미분 - 수직 마스크
    dst4 = cv2.Sobel(np.float32(image), cv2.CV_32F, 0, 1, 3)  # y방향 미분 - 수평 마스크
    dst3 = cv2.convertScaleAbs(dst3)  # 절댓값 및 uint8 형변환
    dst4 = cv2.convertScaleAbs(dst4)
    cv2.imshow("dst- sobel edge", dst)
    cv2.imshow("dst1- vertical_mask", dst1)
    cv2.imshow("dst2- horizontal_mask", dst2)
    cv2.imshow("dst3- vertical_OpenCV", dst3)
    cv2.imshow("dst4- horizontal_OpenCV", dst4)
    cv2.waitKey(0)
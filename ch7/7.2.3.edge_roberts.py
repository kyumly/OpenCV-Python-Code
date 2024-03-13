import cv2
import numpy as np


def masking(img, mask):
    x, y = img.shape
    mask_x, mask_y = mask.shape
    dst = np.zeros((x, y), np.float32)
    mask_x_center, mask_y_center =mask_x //2, mask_y //2
    for i in range(mask_x_center, x - mask_x_center):
        x1, x2 = i - mask_x_center, i + mask_x_center + 1

        for j in range(mask_y_center, y - mask_y_center):
            y1, y2 = j - mask_y_center, j+ mask_y_center + 1

            roi = img[x1:x2,y1:y2].astype(np.float32)
            tem = roi * mask
            dst[i,j]= cv2.sumElems(tem)[0]
    return dst

def differential(image, data1, data2):
    mask1 = np.array(data1, np.float32).reshape(3, 3)
    mask2 = np.array(data2, np.float32).reshape(3, 3)

    dst1 = masking(image, mask1)
    dst2 = masking(image, mask2)


    dst = cv2.magnitude(dst1, dst2)                # 회선 결과인 두 행렬의 크기 계산
    dst1, dst2 = np.abs(dst1), np.abs(dst2)  # 회선 결과 행렬 양수 변경

    dst = np.clip(dst, 0, 255).astype("uint8")
    dst1 = np.clip(dst1, 0, 255).astype("uint8")
    dst2 = np.clip(dst2, 0, 255).astype("uint8")
    return dst, dst1, dst2

if __name__ == '__main__':
    img = cv2.imread('img/edge.jpg', cv2.IMREAD_GRAYSCALE)
    data1 = [-1, 0, 0,
             0, 1, 0,
             0, 0, 0]
    data2 = [0, 0, -1,
             0, 1, 0,
             0, 0, 0]

    a = np.array([
        [1,0],
        [1, 0]
    ], dtype=np.float32)

    b = np.array([
        [1, 100],
        [0, 0],
    ], dtype=np.float32)

    dst, dst1, dst2 = differential(img, data1, data2)
    cv2.imshow("image", img)
    cv2.imshow("roberts edge", dst)
    cv2.imshow("dst1", dst1)
    cv2.imshow("dst2", dst2)
    cv2.waitKey(0)
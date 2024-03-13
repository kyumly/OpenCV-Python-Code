import cv2
import numpy as np



def masking(img, mask):
    x, y = img.shape
    mask_x, mask_y = mask.shape
    dst = np.zeros((x, y), np.float32)
    mask_x_center, mask_y_center =mask_x //2, mask_y //2
    print(mask_x_center, mask_y_center)
    for i in range(mask_x_center, x - mask_x_center):
        x1, x2 = i - mask_x_center, i + mask_x_center + 1

        for j in range(mask_y_center, y - mask_y_center):
            y1, y2 = j - mask_y_center, j+ mask_y_center + 1

            roi = img[x1:x2,y1:y2].astype(np.float32)
            tem = roi * mask
            dst[i,j]= cv2.sumElems(tem)[0]
    return dst



if __name__ == '__main__':
    img = cv2.imread('img/filter_sharpen.jpg', cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise Exception("이미지 없음")

    data1 = [0, -1, 0,
             -1, 5, -1,
             0, -1, 0]
    data2 = [[-1, -1, -1],
             [-1, 9, -1],
             [-1, -1, -1]]
    mask1 = np.array(data1, np.float32).reshape(3, 3)
    mask2 = np.array(data2, np.float32)

    sharpen1 = masking(img, mask1)  # 회선 수행 – 저자 구현 함
    sharpen2 = masking(img, mask2)
    sharpen1 = cv2.convertScaleAbs(sharpen1)
    sharpen2 = cv2.convertScaleAbs(sharpen2)

    cv2.imshow("image", img)
    cv2.imshow("sharpen1", cv2.convertScaleAbs(sharpen1))  # 윈도우 표시 위한 형변환
    cv2.imshow("sharpen2", cv2.convertScaleAbs(sharpen2))
    cv2.waitKey(0)
import numpy as np,cv2

if __name__ == '__main__':
    img = cv2.imread('img/laplacian.jpg', cv2.IMREAD_GRAYSCALE)

    data1 = [
        [0,1,0],
        [1, 4, 1],
        [0, 1, 0],
    ]
    data2 = [
        [-1,-1,-1],
        [-1, 8,-1],
        [-1,-1,-1],
    ]

    mask4 = np.array(data1, np.int16)  # 음수가 있으므로 자료형이 int8인 행렬 선언
    mask8 = np.array(data2, np.int16)


    dst1 = cv2.filter2D(img, cv2.CV_16S, mask4)
    dst2 = cv2.filter2D(img, cv2.CV_16S, mask8)
    dst3 = cv2.Laplacian(img, cv2.CV_16S, 1)

    cv2.imshow('image', img)
    cv2.imshow("filter 2D 4-D", cv2.convertScaleAbs(dst1))
    cv2.imshow("filter 2D 8-D", cv2.convertScaleAbs(dst2))
    cv2.imshow("Laplcaian_Opencv", cv2.convertScaleAbs(dst3))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

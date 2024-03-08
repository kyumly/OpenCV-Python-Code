import numpy as np
import cv2 as cv

def filter(image, mask):
    rows, cols = image.shape[:2]
    dst = np.zeros((rows, cols), np.float32)




if __name__ == "__main__":
    data = cv.imread("img/filter_blur.jpg", cv.IMREAD_GRAYSCALE)
    if data is None:
        raise Exception("파일 없음")
    print(10)

    mask = np.zeros((3,3), dtype=np.float32)
    mask[:] = 1/9
    print(mask)

    filter(data, mask)
    cv.imshow("test", data)
    cv.waitKey(0)
    cv.destroyAllWindows()

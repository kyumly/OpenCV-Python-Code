
import numpy as np, cv2
def getGaussianMask(ksize, sigmaX, sigmaY):
    sigma = 0.3 * ((np.array(ksize) - 1.0) * 0.5 - 1.0) + 0.8  # 표준 편차
    if sigmaX <= 0: sigmaX = sigma[0]
    if sigmaY <= 0: sigmaY = sigma[1]

    u = np.array(ksize)//2            # 커널 크기 절반
    x = np.arange(-u[0], u[0]+1, 1)   # x 방향 범위
    y = np.arange(-u[1], u[1]+1, 1)   # y 방향 범위
    x, y = np.meshgrid(x, y)          # 정방 행렬 생성

    ratio = 1 / (sigmaX*sigmaY * 2 * np.pi)
    v1 = x ** 2 / (2 * sigmaX ** 2)
    v2 = y ** 2 / (2 * sigmaY ** 2 )
    mask = ratio * np.exp(-(v1+v2))  # 2차원 정규 분포 수식
    return mask / np.sum(mask)



image = cv2.imread("img/smoothing.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

ksize = (5, 17)                                        # 크기는 가로x세로로 표현
gaussian_2d = getGaussianMask(ksize, 0, 0)
gaussian_1dX = cv2.getGaussianKernel(ksize[0], 0, cv2.CV_32F)   # 가로 방향 마스크
gaussian_1dY = cv2.getGaussianKernel(ksize[1], 0, cv2.CV_32F)   # 세로 방향 마스크

gauss_img1 = cv2.filter2D(image, -1, gaussian_2d)     # 사용자 생성 마스크 적용
gauss_img2 = cv2.GaussianBlur(image, ksize, 0)
gauss_img3 = cv2.sepFilter2D(image, -1, gaussian_1dX, gaussian_1dY)

titles = ['image','gauss_img1','gauss_img2','gauss_img3']
[cv2.imshow(t, eval(t)) for t in titles]
cv2.waitKey(0)
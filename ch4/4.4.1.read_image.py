import cv2

from common.util import print_matInfo

title1, title2 = "gray2gray", "gray2color"      # 윈도우 이름
gray2gray  = cv2.imread("img/read_gray.jpg", cv2.IMREAD_GRAYSCALE) # 영상 파일 적재
gray2color = cv2.imread("img/read_gray.jpg", cv2.IMREAD_COLOR)

cv2.imshow(title1, gray2gray)
cv2.imshow(title2, gray2color)

if (gray2gray is None or gray2color is None) :  # 예외처리 -영상 파일 읽기 여부 조사
    raise Exception("영상파일 읽기 에러")


# 행렬 내 한 화소 값 표시
print("행렬 좌표 (100, 100) 화소값")
print("화소 shape")
print(f"{title1} : {gray2gray.shape}")
print(f"{title2} : {gray2color.shape}")
print(gray2color[:, 0:2].shape)

print("%s %s" % (title1, gray2gray[100, 100]))
print("%s %s\n" % (title2, gray2color[100, 100]))
print("%s %s\n" % (title2, gray2color[100, 100, :]))


print_matInfo(title1, gray2gray)
print_matInfo(title2, gray2color)

cv2.waitKey(0)
cv2.destroyAllWindows()
import numpy as np, cv2


# %%
def make_palette(rows):
    # 리스트 생성 방식
    hue = [round(i * 180 / rows) for i in range(rows)]  # hue 값 리스트 계산
    hsv = [[(h, 255, 255)] for h in hue]  # (hue, 255,255) 화소값 계산
    hsv = np.array(hsv, np.uint8)  # numpy 행렬의 uint8형 변환

    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)  # HSV 컬러 -> BGR 컬러


def draw_histo_hue(hist, shape=(200, 256, 3)):
    hsv_palate = make_palette(hist.shape[0])  # 색상 팔레트 생성
    hist_img = np.full(shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)  # 정규화

    gap = hist_img.shape[1] / hist.shape[0]  # 한 계급 크기
    for i, h in enumerate(hist):
        x, w = int(round(i * gap)), int(round(gap))
        color = tuple(map(int, hsv_palate[i][0]))  # 정수형 튜플로 변환
        cv2.rectangle(hist_img, (x, 0, w, int(h)), color, cv2.FILLED)  # 팔레트 색으로 그리기

    return cv2.flip(hist_img, 0)


# %%
image = cv2.imread("img/equalize.jpg", cv2.IMREAD_GRAYSCALE)  # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류")
# %%
bins, ranges = [256], [0, 256]
hist = cv2.calcHist([image], [0], None, bins, ranges)  # 히스토그램 계산
# %%
# 히스토그램 누적합 계산
accum_hist = np.zeros(hist.shape[:2], np.float32)
accum_hist[0] = hist[0]
for i in range(1, hist.shape[0]):
    accum_hist[i] = accum_hist[i - 1] + hist[i]

accum_hist = (accum_hist / sum(hist)) * 255  # 누적합의 정규화
dst1 = [[accum_hist[val] for val in row] for row in image]  # 화소값 할당
dst1 = np.array(dst1, np.uint8)

# #numpy 함수 및 룩업 테이블 사용
# accum_hist = np.cumsum(hist)                      # 누적합 계산
# cv2.normalize(accum_hist, accum_hist, 0, 255, cv2.NORM_MINMAX)  # 정규화
# dst1 = cv2.LUT(image, accum_hist.astype("uint8"))  #룩업 테이블로 화소값할당
# %%
dst2 = cv2.equalizeHist(image)  # OpenCV 히스토그램 평활화
hist1 = cv2.calcHist([dst1], [0], None, bins, ranges)  # 히스토그램 계산
hist2 = cv2.calcHist([dst2], [0], None, bins, ranges)  # 히스토그램 계산
hist_img = draw_histo_hue(hist)
hist_img1 = draw_histo_hue(hist1)
hist_img2 = draw_histo_hue(hist2)

# %%
cv2.imshow("image", image)
cv2.imshow("hist_img", hist_img)
cv2.imshow("dst1_User", dst1)
cv2.imshow("User_hist", hist_img1)
cv2.imshow("dst2_OpenCV", dst2)
cv2.imshow("OpenCV_hist", hist_img2)
cv2.waitKey(0)
import numpy as np, cv2

def make_palette(rows):
    # 리스트 생성 방식
    hue = [round(i * 180 / rows) for i in range(rows)]  # hue 값 리스트 계산
    hsv = [[(h, 255, 255)] for h in hue]                # (hue, 255,255) 화소값 계산
    hsv = np.array(hsv, np.uint8)                       # numpy 행렬의 uint8형 변환
    # # 반복문 방식
    # hsv = np.full((rows, 1, 3), (255,255,255), np.uint8)
    # for i in range(0, rows):                                # 행수만큼 반복
    #     hue = round(i / rows * 180 )                        # 색상 계산
    #     hsv[i] = (hue, 255, 255)                            # HSV 컬러 지정

    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)         # HSV 컬러 -> BGR 컬러


def draw_histo_hue(hist, shape=(200, 256,3)):
    hsv_palate = make_palette(hist.shape[0])                      # 색상 팔레트 생성
    hist_img = np.full(shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX)    # 정규화

    gap = hist_img.shape[1] / hist.shape[0]  # 한 계급 크기
    for i, h in enumerate(hist):
        x, w = int(round(i * gap)), int(round(gap))
        color = tuple(map(int, hsv_palate[i][0]))                    # 정수형 튜플로 변환
        cv2.rectangle(hist_img, (x,0,w, int(h) ), color , cv2.FILLED) # 팔레트 색으로 그리기

    return cv2.flip(hist_img, 0)

def search_value_idx(hist, bias = 0):
    for i in range(hist.shape[0]):
        idx = np.abs(bias - i)                     # 검색 위치 (처음 또는 마지막)
        if hist[idx] > 0:  return idx                             # 위치 반환
    return -1                                      # 대상 없으면 반환


image = cv2.imread("img/dst.jpg", cv2.IMREAD_GRAYSCALE)   # 영상읽기
if image is None: raise Exception("영상 파일 읽기 오류")

bsize, ranges = [64], [0,256]                        # 계급 개수 및 화소 범위
hist = cv2.calcHist([image], [0], None, bsize, ranges)

bin_width  = ranges[1]/bsize[0]                      # 계급 너비
print(bin_width)
high = search_value_idx(hist, bsize[0] - 1) * bin_width
print("높은점 : ", high)
low  = search_value_idx(hist, 0)* bin_width
print("낮은 점 : ", low)

idx = np.arange(0, 256)
idx = (idx - low) * 255/(high-low)	# 수식 적용하여 인덱스 생성

idx[0:int(low)] = 0
idx[int(high+1):] = 255

print(idx.shape)
#dst = cv2.LUT(image, idx.astype('uint8'))
## 룩업 테이블 사용하지 않고 직접 구현
dst = np.zeros(image.shape, dtype=image.dtype)
n = 0
for i in range(dst.shape[0]):
    for j in range(dst.shape[1]):
        n += 1
        print(image[i,j ])
        dst[i,j] = idx[image[i,j]]
print(n444e)
hist_dst = cv2.calcHist([dst], [0], None, bsize, ranges)  # 결과 영상 히스토그램 재계산
hist_img = draw_histo_hue(hist, (200,360))          # 원본 영상 히스토그램 그리기
hist_dst_img = draw_histo_hue(hist_dst,(200,360))  # 결과 영상 히스토그램 그리기

print("high_value = ", high)
print("low_value = " , low)
cv2.imshow("image", image)
cv2.imshow("hist_img", hist_img)
cv2.imshow("dst", dst)
cv2.imshow("hist_dst_img", hist_dst_img)
cv2.waitKey(0)
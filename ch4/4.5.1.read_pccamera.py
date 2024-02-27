import cv2

def put_string(frame, text, pt, value, color=(120, 200, 90)): # 문자열 출력 함수 - 그림자 효과
    text += str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0.7, (0, 0, 0), 2)  # 그림자 효과
    cv2.putText(frame, text, pt, font, 0.7, (120, 200, 90), 2)  # 글자 적기

# put_string() 함수는 text 문자와 value 숫자를 pt 좌표에 글자로 적는다
# 같은 문자열을 본래 위치와 2화소 이동된 위치에서 각각 그리기 해서 그림자 효과를 준다

capture = cv2.VideoCapture(0)  # 0번 카메라 연결
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")

# 카메라 속성 획득 및 출력
print("너비 %d" % capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print("높이 %d" % capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("노출 %d" % capture.get(cv2.CAP_PROP_EXPOSURE))
print("밝기 %d" % capture.get(cv2.CAP_PROP_BRIGHTNESS))


while True:  # 무한 반복
    ret, frame = capture.read()  # 카메라 영상 받기
    if not ret:
        break

    if cv2.waitKey(30) >= 0:
        break

    exposure = capture.get(cv2.CAP_PROP_EXPOSURE)
    print(exposure)
    put_string(frame, "EXPOS: ", (10, 40), exposure)
    title = "View Frame from Camera"
    cv2.imshow(title, frame)  # 윈도우에 영상 띄우기
capture.release()

# 카메라에서  cv2.VideoCapture.read()  메서드로 카메라에서 프레임을 받아오며, 2춰놋 튜플로 반환되는데 ret와 frame로 나누어 반환받는다
# ret이 true이면 frmae에 정상적으로 영상 프레임을 가져온 것이다 q

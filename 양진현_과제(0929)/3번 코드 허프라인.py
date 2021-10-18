import cv2
import numpy as np

cap=cv2.VideoCapture("videos/challenge.mp4")

if cap.isOpened()==False:
    print("카메라를 열 수 없습니다")
    exit(1)


while True:

    rt,img_frame=cap.read()

    # 동영상이 끝나면 재생되는 프레임의 위치를 0으로 다시 지정
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    img_gray = cv2.cvtColor(img_frame, cv2.COLOR_BGR2GRAY)
    # 이미지 블러
    img_gray = cv2.GaussianBlur(img_gray, (5, 5), 0)
    # 이진화 수행
    _, img_binary = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
    img_canny = cv2.Canny(img_binary, 50, 150)
    # 사다리꼴 적용하기
    img_roi = img_canny
    rho = 2
    theta = 1 * np.pi / 180
    threshold = 15
    min_line_length = 10
    max_line_gap = 20
    lines = cv2.HoughLinesP(img_roi, rho, theta, threshold,
                            minLineLength=min_line_length,
                            maxLineGap=max_line_gap)
    for i, line in enumerate(lines):
        cv2.line(img_frame, (line[0][0], line[0][1]),
                 (line[0][2], line[0][3]), (0, 255, 0), 2)

    cv2.imshow('Color', img_frame)


    key=cv2.waitKey(33)#waitkey(time(ms)),즉 33밀리세컨드마다 동영상을 재생하기위한 장치
    if key==27:
        break
# 이미지를 BGR에서 HSV로 색변환


cv2.waitKey(0)
cv2.destroyAllWindows()

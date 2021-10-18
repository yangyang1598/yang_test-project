import cv2
import numpy as np
trap_bottom_w=0.8
trap_top_w=0.1
trap_height=0.4
cap=cv2.VideoCapture("videos/challenge.mp4")

if cap.isOpened()==False:
    print("카메라를 열 수 없습니다")
    exit(1)



while True:

    rt,img_frame=cap.read()

    # 동영상이 끝나면 재생되는 프레임의 위치를 0으로 다시 지정
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    img_mask = np.zeros_like(img_frame)
    h,w = img_mask.shape[:2]

    mask_color = (255, 255, 255)
    pts = np.array([[ \
        ((w * (1 - trap_bottom_w)) // 2, h), \
        ((w * (1 - trap_top_w)) // 2, (1 - trap_height) * h), \
        (w - (w * (1 - trap_top_w)) // 2, (1 - trap_height) * h), \
        (w - (w * (1 - trap_bottom_w)) // 2, h)]], \
        dtype=np.int32)  # 정수형으로 조정


    img_hsv = cv2.cvtColor(img_frame, cv2.COLOR_BGR2HSV)  # HSV
    # 채도,명도 정하기
    sy_min = 100;
    sy_max = 255
    vy_min = 100;
    vy_max = 255

    lower_yellow = (10, sy_min, vy_min)  # 자료형은 튜플형태로(H,S,V)
    upper_yellow = (40, sy_max, vy_max)  # 자료형은 튜플형태로(H,S,V)
    img_mask1 = cv2.inRange(img_hsv, lower_yellow, upper_yellow)
    img_yellow = cv2.bitwise_and(img_frame, img_frame, mask=img_mask1)
    bgr_threshold = [200, 200, 200]
    img_dst_w = np.copy(img_frame)
    # BGR 제한 값보다 작으면 검은색으로
    thresholds = (img_frame[:, :, 0] < bgr_threshold[0]) \
                 | (img_frame[:, :, 1] < bgr_threshold[1]) \
                 | (img_frame[:, :, 2] < bgr_threshold[2])

    img_dst_w[thresholds] = [0, 0, 0]

    img_mask3 = cv2.addWeighted(img_yellow, 1.0, img_dst_w, 1.0, 0)

    src = cv2.fillPoly(img_mask, pts, (255, 255, 255))
    img_carline = cv2.bitwise_and(img_mask3,src)

    cv2.imshow('Color', img_carline)


    key=cv2.waitKey(33)#waitkey(time(ms)),즉 33밀리세컨드마다 동영상을 재생하기위한 장치
    if key==27:
        break
# 이미지를 BGR에서 HSV로 색변환


cv2.waitKey(0)
cv2.destroyAllWindows()

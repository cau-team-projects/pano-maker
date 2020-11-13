import numpy as np
import cv2

CAM_CNT = 4
DURATION = 10
cnt = 0
cam = 0
cap = cv2.VideoCapture(0)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
cams = np.zeros((CAM_CNT, height, width, 3), dtype='uint8')

while(True):
    ret, frame = cap.read()
    cams[cam] = frame
    #cams[cam] = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    for i in range(CAM_CNT):
        cv2.imshow('frame' + str(i), cams[i])

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cnt == 0:
        cam += 1
        cam %= CAM_CNT

    cnt += 1
    cnt %= DURATION

cap.release()
cv2.destroyAllWindows()

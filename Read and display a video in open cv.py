import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.avi')

while True:
    ret,frame = cap.read()
    if ret == False:
        print('There is some error...trying again...')
        continue
    cv2.imshow('Inter',frame)
    if cv2.waitKey(40)&0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# -*- coding: UTF-8 -*-
"""
@author:Jaiyaun
@software: PyCharm
@file:task1.py
@time:2021/11/24
"""
import cv2
from datetime import datetime

capture = cv2.VideoCapture(0)

while (True):
    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', gray)
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
    elif key == ord('s'):
        ret = cv2.imwrite("frame_%s.png" % str(datetime.now().strftime("%Y%m%d%H%M%S")), frame)
        print("frame_%s.png" % datetime.now().strftime("%Y%m%d%H%M%S"), ret)

capture.release()
cv2.destroyAllWindows()

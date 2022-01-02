# -*- coding: UTF-8 -*-
"""
@author:Jaiyaun
@software: PyCharm
@file:task2.py
@time:2021/11/24
"""
import cv2
import numpy as np

capture = cv2.VideoCapture(0)

# 在HSV中Blue、Green、Red的范围：
lower_blue = np.array([100, 110, 110])
upper_blue = np.array([130, 255, 255])

lower_green = np.array([40, 90, 90])
upper_green = np.array([70, 255, 255])

lower_red = np.array([160, 120, 120])
upper_red = np.array([179, 255, 255])

while (True):
    # 捕获
    ret, frame = capture.read()

    # 转换HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_red = cv2.inRange(hsv, lower_red, upper_red)

    # 所有mask相加，就可以同时显示
    mask = mask_blue + mask_green + mask_red

    # 保留原图中三种颜色的部分
    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

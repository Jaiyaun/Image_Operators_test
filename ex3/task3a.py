# -*- coding: UTF-8 -*-
"""
@author:Jaiyaun
@software: PyCharm
@file:task3a.py
@time:2021/11/24
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import watermark

img = cv2.imread('shapes.jpg', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)

# 检测圆的位置
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 50, param2=30)
circles = np.uint16(np.around(circles))

drawing = img.copy()
for i in circles[0, :]:
    # 画外圆
    cv2.circle(drawing, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # 画圆心
    cv2.circle(drawing, (i[0], i[1]), 2, (0, 0, 255), 3)

titles = ['Original', 'Edges', 'Statistics Hough']
images = [img, edges, drawing]

for i in range(3):
    plt.subplot(1, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i], fontsize=8)
    plt.xticks([])
    plt.yticks([])

# 保存图片
# watermark.addwatermark(plt, '201944008236Jaiyaun')
watermark.savefig(plt, 'task3a.png', '201944008236Jaiyaun')
plt.show()
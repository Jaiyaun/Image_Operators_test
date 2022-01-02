# -*- coding: UTF-8 -*-
"""
@author:Jaiyaun
@software: PyCharm
@file:task3b.py
@time:2021/11/24
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt
import watermark

img = cv2.imread('stairs.jpg', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)

standard = np.zeros(img.shape, np.uint8)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(standard, (x1, y1), (x2, y2), (0, 0, 255))

statistics = img.copy()
lines = cv2.HoughLinesP(edges, 0.8, np.pi / 180, 90, minLineLength=50, maxLineGap=10)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(statistics, (x1, y1), (x2, y2), (0, 255, 0), 1, lineType=cv2.LINE_AA)

titles = ['Original', 'Edges', 'Standard Hough', 'Statistics Hough']
images = [img, edges, standard, statistics]

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i], fontsize=8)
    plt.xticks([])
    plt.yticks([])

# 保存图片
# watermark.addwatermark(plt, '201944008236Jaiyaun')
watermark.savefig(plt, 'task3a.png', '201944008236Jaiyaun')
plt.show()

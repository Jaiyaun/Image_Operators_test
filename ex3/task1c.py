# -*- coding: UTF-8 -*-
"""
@author:Jaiyaun
@software: PyCharm
@file:task1c.py
@time:2021/11/17
"""

import cv2
import matplotlib.pyplot as plt
import watermark

# 读入图像
img = cv2.imread('noisy.jpg', 0)

# 固定阈值法
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# Otsu阈值法
ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# 先进行高斯滤波，再使用Otsu阈值法
blur = cv2.GaussianBlur(img, (5, 5), 0)
ret3, th3 = cv2.threshold(blur, 105, 255, cv2.THRESH_BINARY)
ret4, th4 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

images = [img, 0, th1, img, 0, th2, blur, 0, th3, blur, 0, th4]
titles = ['Original', 'Histogram', 'Global(v=105)',
          'Original', 'Histogram', "Otsu's",
          'Gaussian filterra Image', 'Histogram', 'Global(v=105)',
          'Gaussian filterra Image', 'Histogram', "Otsu's",]

for i in range(4):
    # 绘制原图
    plt.subplot(4, 3, i * 3 + 1)
    plt.imshow(images[i * 3], 'gray')
    plt.title(titles[i * 3], fontsize=8)
    plt.xticks([])
    plt.yticks([])

    # 绘制直方图
    plt.subplot(4, 3, i * 3 + 2)
    plt.hist(images[i * 3].ravel(), 256)
    plt.title(titles[i * 3 + 1], fontsize=8)
    plt.xticks([])
    plt.yticks([])

    # 绘制阈值图
    plt.subplot(4, 3, i * 3 + 3)
    plt.imshow(images[i * 3 + 2], 'gray')
    plt.title(titles[i * 3 + 2], fontsize=8)
    plt.xticks([])
    plt.yticks([])

# 保存图片
# watermark.addwatermark(plt, '201944008236Jaiyaun')
watermark.savefig(plt, 'task1c.png', '201944008236Jaiyaun')
plt.show()
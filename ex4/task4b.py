# -*- coding: UTF-8 -*-
"""
@author:Jaiyaun
@software: PyCharm
@file:task4b.py
@time:2021/11/24
"""
import cv2
import matplotlib.pyplot as plt
import watermark

src = cv2.imread('natrescene.jpg')
dst = cv2.pyrMeanShiftFiltering(src, 25, 40, None, 2)

titles = ['Orignal', 'Mean-Shift clustering']
images = [src, dst]

for i in range(2):
    plt.subplot(1, 2, i + 1)
    # 灰度图只是二维矩阵因此.shape只有两个参数
    if len(images[i].shape) < 3:
        plt.imshow(images[i], 'gray')
    else:
        plt.imshow(images[i][..., ::-1])
    plt.title(titles[i], fontsize=8)
    plt.xticks([])
    plt.yticks([])

# 保存图片
# watermark.addwatermark(plt, '201944008236Jaiyaun')
watermark.savefig(plt, 'task4b.png', '201944008236Jaiyaun')
plt.show()
# -*- coding: UTF-8 -*-
"""
@author:Jaiyaun
@software: PyCharm
@file:task3a.py
@time:2021/11/24
"""

import matplotlib.pyplot as plt
import cv2
import watermark

img = cv2.imread('scene.jpg', cv2.IMREAD_COLOR)

# 色调H，饱和度为S，光强为V
hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
# 函数 cv2.split() 传入一个图像数组，并将图像拆分为 B/G/R 三个通道
channels = cv2.split(hls)
equalized_l = cv2.equalizeHist(channels[1], channels[1])
cv2.merge(channels, hls)
dst = cv2.cvtColor(hls, cv2.COLOR_HLS2BGR)

titles = ['Original', 'H', 'L', 'S', 'EqualiezdL', 'Equaliezd']
images = [img, hls[:, :, 0], hls[:, :, 1], hls[:, :, 2], equalized_l, dst]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    if len(images[i].shape) < 3:
        plt.imshow(images[i], 'gray')
    else:
        plt.imshow(images[i][..., ::-1])
    plt.title(titles[i], fontsize=8)
    plt.xticks([])
    plt.yticks([])

# 保存图片
# watermark.addwatermark(plt, '201944008236Jaiyaun')
watermark.savefig(plt, 'task3a.png', '201944008236Jaiyaun')
plt.show()

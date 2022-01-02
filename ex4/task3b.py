# -*- coding: UTF-8 -*-
"""
@author:Jaiyaun
@software: PyCharm
@file:task3b.py
@time:2021/11/24
"""
import matplotlib.pyplot as plt
import cv2
import watermark

img = cv2.imread('scene.jpg', cv2.IMREAD_COLOR)

channels = cv2.split(img)
equalized_b = cv2.equalizeHist(channels[0], channels[0])
equalized_g = cv2.equalizeHist(channels[1], channels[1])
equalized_r = cv2.equalizeHist(channels[2], channels[2])
dst = cv2.merge(channels)

titles = ['Original', 'Equalized',
          'R', 'EqualizedR',
          'G', 'EqualiezdG',
          'B', 'EqualiezdB']
images = [img, dst,
          channels[2], equalized_r,
          channels[1], equalized_g,
          channels[0], equalized_b]

for i in range(8):
    plt.subplot(2, 4, i + 1)
    if len(images[i].shape) < 3:
        plt.imshow(images[i], 'gray')
    else:
        plt.imshow(images[i][..., ::-1])
    plt.title(titles[i], fontsize=8)
    plt.xticks([])
    plt.yticks([])

# 保存图片
# watermark.addwatermark(plt, '201944008236Jaiyaun')
watermark.savefig(plt, 'task3b.png', '201944008236Jaiyaun')
plt.show()

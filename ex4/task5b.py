# -*- coding: UTF-8 -*-
"""
@author:Jaiyaun
@software: PyCharm
@file:task5b.py
@time:2021/11/24
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np
import watermark

img_gray = cv2.imread('goldhill.png', cv2.IMREAD_GRAYSCALE)

lut = np.zeros((256, 1, 3), dtype=np.uint8)

table = np.zeros((1, 256), img_gray.dtype)
print(table.shape)

for i in range(len(table[0])):
    # 将每个元素的原始灰度值翻转
    table[0][i] = 255 - i

dst = cv2.LUT(img_gray, table)

titles = ['Original', 'Color']
images = [img_gray, dst]

for i in range(2):
    plt.subplot(1, 2, i + 1)
    if len(images[i].shape) < 3:
        plt.imshow(images[i], 'gray')
    else:
        plt.imshow(images[i][..., ::-1])
    plt.title(titles[i], fontsize=8)
    plt.xticks([])
    plt.yticks([])

# 保存图片
# watermark.addwatermark(plt, '201944008236Jaiyaun')
watermark.savefig(plt, 'task5b.png', '201944008236Jaiyaun')
plt.show()

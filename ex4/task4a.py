# -*- coding: UTF-8 -*-
"""
@author:Jaiyaun
@software: PyCharm
@file:task4a.py
@time:2021/11/24
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import watermark

img = cv2.imread('natrescene.jpg', cv2.IMREAD_COLOR)

# 二维图像转换成一维
data = img.reshape((-1, 3))
data = np.float32(data)

# 定义中心
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

# 设置标签
flags = cv2.KMEANS_RANDOM_CENTERS

# K-Means聚类，2、4、8、16、64
compactness, lables2, centers2 = cv2.kmeans(data, 2, None, criteria, 10, flags)
compactness, lables4, centers4 = cv2.kmeans(data, 4, None, criteria, 10, flags)
compactness, lables8, centers8 = cv2.kmeans(data, 8, None, criteria, 10, flags)
compactness, lables16, centers16 = cv2.kmeans(data, 16, None, criteria, 10, flags)
compactness, lables64, centers64 = cv2.kmeans(data, 64, None, criteria, 10, flags)

# 一维图像转换回二维
centers2 = np.uint8(centers2)
res = centers2[lables2.flatten()]
dst2 = res.reshape(img.shape)

centers4 = np.uint8(centers4)
res = centers4[lables4.flatten()]
dst4 = res.reshape(img.shape)

centers8 = np.uint8(centers8)
res = centers8[lables8.flatten()]
dst8 = res.reshape(img.shape)

centers16 = np.uint8(centers16)
res = centers16[lables16.flatten()]
dst16 = res.reshape(img.shape)

centers64 = np.uint8(centers64)
res = centers64[lables64.flatten()]
dst64 = res.reshape(img.shape)

titles = ['Original', 'K=2', 'K=4', 'K=8', 'K=16', 'K=64']
images = [img, dst2, dst4, dst8, dst16, dst64]

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
watermark.savefig(plt, 'task4a.png', '201944008236Jaiyaun')
plt.show()

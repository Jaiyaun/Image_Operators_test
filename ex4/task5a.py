# -*- coding: UTF-8 -*-
"""
@author:Jaiyaun
@software: PyCharm
@file:task5a.py
@time:2021/11/24
"""
import cv2
import matplotlib.pyplot as plt
import watermark


def colormap_name(id):
    switcher = {
        0: "COLORMAP_AUTUMN",
        1: "COLORMAP_BONE",
        2: 'COLORMAP_JET',
        3: 'COLORMAP_WINTER',
        4: 'COLORMAP_RAINBOW',
        5: 'COLORMAP_OCEAN',
        6: 'COLORMAP_SUMMER',
        7: 'COLORMAP_SPRING',
        8: 'COLORMAP_COOL',
        9: 'COLORMAP_HSV',
        10: 'COLORMAP_PINK',
        11: 'COLORMAP_HOT'
    }
    return switcher.get(id, "NONE")


img = cv2.imread('goldhill.png', cv2.IMREAD_GRAYSCALE)

for i in range(0, 4):
    for j in range(0, 3):
        k = i + j * 4
        img_color = cv2.applyColorMap(img, k)
        plt.subplot(4, 3, k + 1)
        plt.imshow(img_color[..., ::-1])
        plt.title(colormap_name(k), fontsize=8)
        plt.xticks([])
        plt.yticks([])

# 保存图片
# watermark.addwatermark(plt, '201944008236Jaiyaun')
watermark.savefig(plt, 'task5a.png', '201944008236Jaiyaun')
plt.show()

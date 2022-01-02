# -*- coding: UTF-8 -*-
"""
@author:Jaiyaun
@software: PyCharm
@file:task2.py
@time:2021/11/17
"""

import cv2
import matplotlib.pyplot as plt
import watermark

img = cv2.imread('coins.jpg')
shifted = cv2.pyrMeanShiftFiltering(img, 21, 51)

gray = cv2.cvtColor(shifted, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
print("[INFO] {} unique cintours found".format(len(cnts)))

labeled_image = img.copy()
for (i, c) in enumerate(cnts):
    ((x, y), _) = cv2.minEnclosingCircle(c)
    cv2.putText(labeled_image, "#{}".format(i + 1), (int(x) - 10, int(y)),
                cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 255), 2)
    cv2.drawContours(labeled_image, [c], -1, (0, 255, 0), 2)

titles = ['Original', 'MeanShiftFiltering', 'Gray', 'OTSU', 'Labeled']
images = [img, shifted, gray, thresh, labeled_image]

for i in range(5):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i], fontsize=8)
    plt.xticks([])
    plt.yticks([])

# 保存图片
# watermark.addwatermark(plt, '201944008236Jaiyaun')
watermark.savefig(plt, 'task2.png', '201944008236Jaiyaun')
plt.show()
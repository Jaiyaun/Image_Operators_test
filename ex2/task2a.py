import cv2
from matplotlib import pyplot as plt
import numpy as np

def savefig(plt, filename):
    fig = plt.gcf()
    fig.text(0.8, 0.05, '201944008236杨家源', fontsize=40, rotation=30, color='blue', ha='right', va='bottom', alpha=0.2)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.subplots_adjust(top=1, bottom=0, right=1,left=0,hspace=0,wspace=0)
    plt.margins(0, 0)
    fig.savefig(filename, format='png', transparent=True, dpi=300, pad_inches=0)

def linearTransfer(img, a, b):
    new = np.uint8(np.clip((a * img + b), 0, 255))
    return new

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
img = cv2.imread('lena.png',0)

# 原图
plt.figure(figsize=(10, 10))
plt.subplot(231)
plt.imshow(img, cmap="gray")
plt.title("Original")
# 灰度变化
plt.subplot(232)
img1 = linearTransfer(img, 1, 30)
plt.imshow(img1, cmap="gray")
plt.title("a=1 b=30")

plt.subplot(233)
img2 = linearTransfer(img, 1.5, 0)
plt.imshow(img2, cmap="gray")
plt.title("a=1.5 b=0")

plt.subplot(234)
img3 = linearTransfer(img, 0.2, 0)
plt.imshow(img3, cmap="gray")
plt.title("a=0.2 b=0")

plt.subplot(235)
img4 = linearTransfer(img, -1, 255)
plt.imshow(img4, cmap="gray")
plt.title("a=-1 b=255")

plt.subplot(236)
img5 = linearTransfer(img, 1.5, 10)
plt.imshow(img5, cmap="gray")
plt.title("a=1.5 b=10")

# 保存图片
savefig(plt, "task2a.png")
plt.show()

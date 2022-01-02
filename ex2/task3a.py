import cv2
from matplotlib import pyplot as plt
from skimage.util import random_noise as rdns

def savefig(plt, filename):
    fig = plt.gcf()
    fig.text(0.8, 0.05, '201944008236杨家源', fontsize=40, rotation=30, color='blue', ha='right', va='bottom', alpha=0.2)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.subplots_adjust(top=1, bottom=0, right=1,left=0,hspace=0,wspace=0)
    plt.margins(0, 0)
    fig.savefig(filename, format='png', transparent=True, dpi=300, pad_inches=0)

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
img = cv2.imread('lena.png', 0)

plt.figure(figsize=(6*img.shape[1] / 300, 6*img.shape[0] / 300), dpi=300)

# 原图
plt.subplot(231)
plt.title("Original")
plt.imshow(img, cmap="gray")
plt.axis("off")

# 加入噪点
plt.subplot(232)
noise1 = rdns(img, mode='gaussian', seed=None, clip=True)
plt.imshow(noise1, cmap="gray")
plt.title("Gaussian")
plt.axis("off")

plt.subplot(233)
noise2 = rdns(img, mode='salt', amount=0.1)
plt.imshow(noise2, cmap="gray")
plt.title("Salt")
plt.axis("off")

plt.subplot(234)
noise3 = rdns(img, mode='pepper', amount=0.1)
plt.imshow(noise3, cmap="gray")
plt.title("Pepper")
plt.axis("off")

plt.subplot(235)
noise4 = rdns(img, mode='s&p', amount=0.1)
plt.imshow(noise4, cmap="gray")
plt.title("S&P")
plt.axis("off")

plt.subplot(236)
noise5 = rdns(img, mode='speckle', seed=None, clip=True)
plt.imshow(noise5, cmap="gray")
plt.title("Speckle")
plt.axis("off")

# 保存图片
savefig(plt, "task3a.png")
plt.show()
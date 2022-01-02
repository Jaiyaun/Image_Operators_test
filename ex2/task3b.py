import cv2
from matplotlib import pyplot as plt
import numpy as np
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

# 加入噪点
noise1 = rdns(img, mode='gaussian', seed=None, clip=True)
noise1 = np.array(255 * noise1, dtype='uint8')

noise2 = rdns(img, mode='salt', amount=0.1)
noise2 = np.array(255 * noise2, dtype='uint8')

noise3 = rdns(img, mode='pepper', amount=0.1)
noise3 = np.array(255 * noise3, dtype='uint8')

noise4 = rdns(img, mode='s&p', amount=0.1)
noise4 = np.array(255 * noise4, dtype='uint8')

noise5 = rdns(img, mode='speckle', seed=None, clip=True)
noise5 = np.array(255 * noise5, dtype='uint8')

imgs = [img, noise1, noise2, noise3, noise4, noise5]
titles = ['original', 'gaussian', 'pepper', 'salt', 's&p', 'speckle']

plt.figure(figsize=(6 * img.shape[1] / 300, 6 * img.shape[0] / 300), dpi=300)
# 均值滤波器
for i in range(6):
    img_mean = cv2.blur(imgs[i], (5, 5))
    plt.subplot(2, 3, i + 1)
    plt.imshow(img_mean, cmap='gray')
    plt.title(titles[i] + ' blur')
    plt.axis('off')
# 保存图片
savefig(plt, "task3b1.png")

plt.figure(figsize=(6 * img.shape[1] / 300, 6 * img.shape[0] / 300), dpi=300)
# 高斯滤波器
for i in range(6):
    img_Guassian = cv2.GaussianBlur(imgs[i], (5, 5), 0)
    plt.subplot(2, 3, i + 1)
    plt.imshow(img_Guassian, cmap='gray')
    plt.title(titles[i] + ' guass')
    plt.axis('off')
# 保存图片
savefig(plt, "task3b2.png")

plt.figure(figsize=(6 * img.shape[1] / 300, 6 * img.shape[0] / 300), dpi=300)
# 中值滤波器
for i in range(6):
    img_median = cv2.medianBlur(imgs[i], 5)
    plt.subplot(2, 3, i + 1)
    plt.imshow(img_median, cmap='gray')
    plt.title(titles[i] + ' med')
    plt.axis('off')
# 保存图片
savefig(plt, "task3b3.png")

plt.figure(figsize=(6 * img.shape[1] / 300, 6 * img.shape[0] / 300), dpi=300)
# 双边滤波
for i in range(6):
    img_bilater = cv2.bilateralFilter(imgs[i], 9, 75, 75)
    plt.subplot(2, 3, i + 1)
    plt.imshow(img_bilater, cmap='gray')
    plt.title(titles[i] + ' bil')
    plt.axis('off')
# 保存图片
savefig(plt, "task3b4.png")

plt.figure(figsize=(6 * img.shape[1] / 300, 6 * img.shape[0] / 300), dpi=300)
# box滤波器
for i in range(6):
    img_box = cv2.boxFilter(imgs[i], -1, (5, 5))
    plt.subplot(2, 3, i + 1)
    plt.imshow(img_box, cmap='gray')
    plt.title(titles[i] + ' box')
    plt.axis('off')
# 保存图片
savefig(plt, "task3b5.png")

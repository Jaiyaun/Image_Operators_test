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

def gammaTransfer(img, c, v):
    lut = np.zeros(256, dtype=np.float32)
    for i in range(256):
        lut[i] = c * i ** v
    output = cv2.LUT(img, lut)
    output = np.uint8(output + 0.5)

    return output

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
img = cv2.imread('airoport.png',0)

# 原图
fig, (ax, ax2) = plt.subplots(ncols=2)
ax.imshow(img, cmap="gray")
ax.set_title("Original")

# gamma变换
img1 = gammaTransfer(img, 0.00000005, 4.0)
ax2.imshow(img1, cmap="gray")
ax2.set_title("gamma变换")

plt.tight_layout()
plt.setp(plt.gcf().get_axes(), xticks=[], yticks=[])

# 保存图片
savefig(plt, "task2b.png")
plt.show()


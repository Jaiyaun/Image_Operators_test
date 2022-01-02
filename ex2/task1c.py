import cv2
from matplotlib import pyplot as plt
import numpy as np

def savefig(fig, plt, filename):

    fig.text(0.8, 0.05, '201944008236杨家源', fontsize=40, rotation=30, color='lightblue', ha='right', va='bottom', alpha=0.2)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.subplots_adjust(top=1, bottom=0, right=1,left=0,hspace=0,wspace=0)
    plt.margins(0, 0)
    fig.savefig(filename, format='png', transparent=True, dpi=300, pad_inches=0)

plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
img = cv2.imread('island.png',cv2.IMREAD_COLOR)
# 获取灰度图像
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 利用cv2.equalizeHist()进行均衡化
equ = cv2.equalizeHist(gray_img)

# 计算cdf
hist1, bins = np.histogram(equ.ravel(), 256, [0, 256])
cdf = hist1.cumsum()
cdf_normalised = cdf * float(hist1.max() / cdf.max())

# 显示图片
fig, (ax, ax2) = plt.subplots(ncols=2)
ax.imshow(equ, cmap="gray")
ax.set_title('Equalized')
ax2.hist(equ.ravel(), 256, [0, 256], color=[0, 0, 0])
ax2.plot(cdf_normalised)
ax2.set_title('Histogram')

# 调整比例
asp = np.diff(ax2.get_xlim())[0] / np.diff(ax2.get_ylim())[0]
asp = asp * img.shape[0] / img.shape[1]
ax2.set_aspect(asp)
# 显示直方图
plt.show()
# 保存
savefig(fig, plt, "task1c.png")


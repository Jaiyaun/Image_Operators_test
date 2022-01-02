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

# 分离RBG通道
b, g, r = cv2.split(img)

# 显示图片
fig, (ax, ax2) = plt.subplots(ncols=2)
ax.imshow(img[:,:,::-1])
ax.set_title('原图')
ax2.hist(b.ravel(), 256, [0, 256], color=[0, 0, 1, 0.7])
ax2.hist(g.ravel(), 256, [0, 256], color=[0, 1, 0, 0.7])
ax2.hist(r.ravel(), 256, [0, 256], color=[1, 0, 0, 0.7])
ax2.set_title('直方图')

# 调整比例
asp = np.diff(ax2.get_xlim())[0] / np.diff(ax2.get_ylim())[0]
asp = asp * img.shape[0] / img.shape[1]
ax2.set_aspect(asp)
# 显示直方图
plt.show()
# 保存
savefig(fig, plt, "task1a.png")


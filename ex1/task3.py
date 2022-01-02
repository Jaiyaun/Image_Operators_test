import cv2
import numpy as np

def get_red(img):
    redImg = img[:,:,2]
    return redImg

def get_green(img):
    greenImg = img[:,:,1]
    return greenImg

def get_blue(img):
    blueImg = img[:,:,0]
    return blueImg

img = cv2.imread('lena.png')
b = get_blue(img)
g = get_green(img)
r = get_red(img)

# 图片拼接
imgs = np.hstack([b, g, r])
# 展示
cv2.imshow("a", imgs)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 将lena.png中脸部截取出来，在窗口显示出来（用cv2.imshow），并保存为face.png
face = img[125:240,125:220]
cv2.imshow("face",face)
cv2.waitKey(0)
cv2.imwrite('face.png',face)
cv2.destroyAllWindows()

# 将lena.png中帽子部分的红色通道截取出来并显示
hat = img[25:120,50:220]
r = get_red(hat)
cv2.imshow("hat",hat)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 将lena.png原图中帽子部分（步骤c中的部分）的蓝色通道清除，在一个窗口分别显示其R，G，B通道图片和进行灰度变换后的图片
hat1 = hat.copy()
# 清除蓝色通道
hat1[:, :, 0] = 0
# 在一个窗口分别显示其R，G，B通道图片和进行灰度变换后的图片
hat_b = np.zeros((hat1.shape[0], hat1.shape[1]), dtype=hat1.dtype)
hat_g = np.zeros((hat1.shape[0], hat1.shape[1]), dtype=hat1.dtype)
hat_r = np.zeros((hat1.shape[0], hat1.shape[1]), dtype=hat1.dtype)
hat_b[:, :] = hat1[:, :, 0]
hat_g[:, :] = hat1[:, :, 1]
hat_r[:, :] = hat1[:, :, 2]
# 彩色变为灰度图像
hat_gray = cv2.cvtColor(hat1, cv2.COLOR_BGR2GRAY)
# 修改图片尺寸
im1 = cv2.resize(hat_r, (200, 120))
im2 = cv2.resize(hat_g, (200, 120))
im3 = cv2.resize(hat_b, (200, 120))
im4 = cv2.resize(hat_gray, (200, 120))
# 水平拼接
h1 = np.hstack((im1, im2))
h2 = np.hstack((im3, im4))
# 垂直拼接
v1 = np.vstack((h1, h2))
cv2.imshow("test", v1)
cv2.waitKey(0)
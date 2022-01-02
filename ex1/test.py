import cv2

lena = cv2.imread("lena.png")
logo = cv2.imread("logo.png")
# 原图片尺寸太小，放大
lena = cv2.resize(lena, (800, 800))
print(logo.shape)
# 取出相同的ROI
a = lena[0:504, 0:420]
b = logo[0:504, 0:420]
# 将两幅图像进行融合
c = cv2.addWeighted(a, 1, b, 0.5, 1)

cv2.imshow("c", c)
cv2.waitKey(0)
# 替换原图的ROI
lena[0:504, 0:420] = c

cv2.imshow("lena", lena)
cv2.waitKey(0)
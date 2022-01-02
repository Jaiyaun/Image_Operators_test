import cv2
import matplotlib.pyplot as plt

image = cv2.imread('fruits.png')

size = image.shape
print('图像尺寸：',size)
cv2.imshow('201944008236 Jaiyaun',image)

# 输入“s“保存图片 否则退出当前窗口并用plt显示图片
k = cv2.waitKey(0)
if k == ord('s'):
    cv2.imwrite('fruits1.png',image)
else:
    cv2.destroyAllWindows()
    image = plt.imread('lena.png')
    plt.imshow(image)
    plt.show()

# image = plt.imread('fruits.png')
# plt.imshow(image, cmap="gray")
# plt.show()


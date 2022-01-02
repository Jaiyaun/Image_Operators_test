import cv2

img1 = cv2.imread('logo.png')
img2 = cv2.imread('lena.png')
img2 = cv2.resize(img2, (500, 500))

# 利用cv2.addWeighted()函数将两个大小不同的照片混合在一起
# 在lena.png获取和logo.png大小相同的ROI
rows, cols, channels = img1.shape
roi = img2[0:rows, 0:cols]
#进行融合
roi2 = cv2.addWeighted(img1, 0.7, roi, 0.3, 0)
img2[0:rows, 0:cols] = roi2

cv2.imshow('a', img2)
cv2.waitKey(0)

# b
#把logo放在左上角
rows,cols = img1.shape[:2]
roi = img2[0:rows,0:cols]

#创建掩膜
logogray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(logogray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img3 = cv2.bitwise_and(roi,roi,mask = mask_inv)
dst = cv2.add(img1,img3)
img2[0:rows,0:cols] = dst

cv2.imshow('b',img2)
cv2.waitKey(0)

#c
img4 = cv2.bitwise_and(roi,roi,mask = mask_inv)

dst = cv2.add(img1,img4)
dst_1 = cv2.addWeighted(roi,0.7,dst,0.3,1)
img2[0:rows,0:cols] = dst_1

cv2.imshow('c',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

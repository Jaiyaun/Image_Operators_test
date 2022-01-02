import numpy as np
import cv2

img = np.zeros((720,600,3), np.uint8)

cv2.ellipse(img,(300,140),(140,140),300,120,-180,(0,0,255),-1)
cv2.circle(img,(300,140),55,(0,0,0),-1)

cv2.ellipse(img,(140,415),(140,140),300,60,360,(0,255,0),-1)
cv2.circle(img,(140,415),55,(0,0,0),-1)

cv2.ellipse(img,(460,415),(140,140),300,0,300,(255,0,0),-1)
cv2.circle(img,(460,415),55,(0,0,0),-1)

cv2.putText(img,'OpenCV',(80,650),cv2.FONT_HERSHEY_SIMPLEX,3.75,(255,255,255),4)

cv2.rectangle(img, (300,680),(575,700),(0,255,0))
cv2.putText(img,'Created by 201944008236 Yangjiayuan',(305,695),cv2.FONT_HERSHEY_SIMPLEX,0.42,(100,10,120),1)

img1 = cv2.resize(img,dsize = (300,360))

cv2.imshow('test',img)
cv2.waitKey(0)

cv2.imshow('example',img1)
cv2.waitKey(0)
cv2.imwrite('logo.png',img1)


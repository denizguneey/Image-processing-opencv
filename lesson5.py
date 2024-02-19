import cv2
import numpy as np

image=cv2.imread("logo.png")

image[50,30]=[255,255,255]

for i in range(100):
    image[70,i]=[255,255,255]


cv2.imshow("image",image)

cv2.waitKey(0)
cv2.destroyAllWindows()
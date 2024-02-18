import cv2
import numpy as np 

image1= cv2.imread("logo.png")
image2= cv2.imread("newimage.png")

cv2.imshow("image1",image1)

print(image1.size)
print(image1.dtype)
print(image1.shape)


cv2.waitKey(0)
cv2.destroyAllWindows()
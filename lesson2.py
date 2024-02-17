import cv2
import numpy as np 

image= cv2.imread("logo.png")

cv2.imshow("image1",image)

print(image)

cv2.waitKey(0)
cv2.destroyAllWindows()
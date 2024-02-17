import cv2
import numpy as np 

image= cv2.imread("logo.png",0)

cv2.imshow("image1",image)

cv2.imwrite("newimage.png",image)

cv2.waitKey(0)
cv2.destroyAllWindows()
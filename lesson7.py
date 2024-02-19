import cv2
import numpy as np

image= cv2.imread("graph.png")


#add effect to selected area image[y,x]
image[50:150,200:300,0]=255
image[50:150,200:300,1]=255


cv2.imshow("graph",image)


cv2.waitKey(0)
cv2.destroyAllWindows()
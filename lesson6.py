import cv2
import numpy as np

image= cv2.imread("graph.png")

#desired region is cropped
cross=image[50:150,200:300]

cv2.imshow("cross-sectional area",cross)

#the cropped area is added to the desired area in the selected image
image[0:100,0:100]=cross

#RGB effect 0:Blue 1:Green 2:Red
#image[ : ,: ,0]=255
#image[ : ,: ,1]=255
#image[ : ,: ,2]=255

#add color to selected area
image[50:150,200:300]=(0,150,255)

cv2.imshow("graph",image)


cv2.waitKey(0)
cv2.destroyAllWindows()
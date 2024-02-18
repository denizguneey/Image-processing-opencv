import cv2
import numpy as np 

image=cv2.imread("logo.png")

cv2.imshow("image",image)

print(image[(80,80)]) #bgr values ​​at this pixel
print("Size of the image: " +str(image.size))
print("features of the image:"+str(image.shape))
print("datatype of the image:"+str(image.dtype))

cv2.waitKey(0)
cv2.destroyAllWindows()
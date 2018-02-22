import numpy as np
import cv2
from matplotlib import pyplot as plt

# read original image
#keep the image and code in same folder
img = cv2.imread("form3.bmp")

#convert color image to gray scale 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#blur the image to reduce the edge content
blur = cv2.GaussianBlur(gray,(5,5),0)


#OTSU thresholding to convert gray color image into binary
(ret,binary) = cv2.threshold(blur,130,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#define kernel to iterate over the whole image we have taken 3x3 kernal
kernel = np.ones((3,3),np.uint8)

#erode image for removing small white noise, detach two connected objects,
#all the pixels near boundary will be discarded depending upon the size of kernel
erosion = cv2.erode(binary,kernel,iterations = 1)

#close small holes inside the foreground objects,
#remove small black points on the object.
#closing = cv2.morphologyEx(erosion, cv2.MORPH_CLOSE, kernel)

#Save the image
cv2.imwrite("form.png",erosion)
                          

plt.imshow(erosion, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()



"""#To dispaly the image on screen
cv2.namedWindow("output", cv2.WINDOW_NORMAL)
cv2.imshow("output", closing)
cv2.waitKey(0)"""

import cv2 
import numpy as np
import sys
from selecter import*


#To display the preview of the crop image
cv2.namedWindow("Croped image", cv2.WINDOW_NORMAL)    #To display the preview of the crop image
cv2.imshow("Croped image", crop_img)

original = crop_img                                     #imagem original
color_image = crop_img                                  #Cópia da imagem original

#---------Thresh filters------------------------

ret,thresh1 = cv2.threshold(original,127,255,cv2.THRESH_BINARY)
ret,thresh3 = cv2.threshold(original,127,255,cv2.THRESH_TRUNC)

#-----------------Boundaries-------------------
lower = np.array([87, 80, 74])                  #para remover os cinzentos do display3 (nao é ferrugem)
uper = np.array([127, 127, 127])
mask=cv2.inRange(thresh3,lower,uper)
color_image[mask>0] = (0,0,0)

lower_1 = np.array([255, 255, 255])             #para remover os brancos do display1 (nao é ferrugem)
uper_1 = np.array([255, 255, 255])
mask1 = cv2.inRange(thresh1, lower_1, uper_1)
color_image[mask1>0] = (0, 0, 0)

#Display detected areas
cv2.namedWindow("Detected Areas", cv2.WINDOW_NORMAL)
cv2.imshow("Detected Areas", color_image)

#--------------------Evaluate rust intensity------------
gray = color_image.copy()
gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY) 

if len(gray.shape)< 3:
    canais = 1
    height, width = gray.shape
else:
    canais = len(gray.shape)
    height, width, canais = gray.shape

for x in range(height):
  for y in range(width):

    if(gray[x,y]<150 and gray[x,y]>110):
      original[x,y] = [0, 255, 255]
    if(gray[x,y]<110 and gray[x,y]>70):
      original[x,y] = [0, 128, 255]
    if(gray[x,y]<70 and gray[x,y]>0):
      original[x,y] = [0, 0, 255]


#display rust intensity
cv2.namedWindow("Rust Intensity", cv2.WINDOW_NORMAL)
cv2.imshow("Rust Intensity", original)
cv2.waitKey(0)

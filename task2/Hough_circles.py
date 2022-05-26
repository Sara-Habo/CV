# -*- coding: utf-8 -*-
"""
Created on Fri May 27 00:07:17 2022

@author: Dell
"""

import numpy as np
import cv2 
import matplotlib.pyplot as plt
def Hough_Circle(img):
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #convert to gray
    gray = cv2.medianBlur(gray,9) #smoothing, if not applied or reducedthere is more false circles
    
    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,105,
                                param1=50,param2=34,minRadius=0,maxRadius=0)
    detected_circles = np.uint16(np.around(circles)) #cast to int after rounding to nearest int 1.6>>1.>>1
    return detected_circles

img1=cv2.imread("shapes.png")
output1=img1.copy()

img2=cv2.imread("circles.jpg")
output2=img2.copy()

detected_circles1=Hough_Circle(img1)
detected_circles2=Hough_Circle(img2)

for (x,y,r) in detected_circles1[0,:]:
    cv2.circle(output1,(x,y),r,(253,7,155),3) #draw line around detected circles ,3>>thickness
    cv2.circle(output1,(x,y),1,(253,7,155),3) #draw center as dot

for (x,y,r) in detected_circles2[0,:]:
    cv2.circle(output2,(x,y),r,(253,7,155),3) #draw line around detected circles ,3>>thickness
    cv2.circle(output2,(x,y),1,(253,7,155),3) #draw center as dot

fig,axs=plt.subplots(1,2,figsize=(12,5))
axs[0].imshow(output1)
axs[1].imshow(output2)
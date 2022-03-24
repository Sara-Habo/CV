# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 21:25:49 2022

@author: Dell
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 19:26:51 2022

@author: Dell
"""

import numpy as np
import matplotlib.pyplot as plt
import cv2
from skimage.color import rgb2gray

def Hist(image): #return the image histogram
    h=np.zeros(shape=(1,256),dtype=int)
    s=image.shape
    for i in range(s[0]):
        for j in range(s[1]):
            k=image[i,j]
            h[0,k]=h[0,k]+1
    return h[0]

def Equalize(freq,max_intensity,image_size): #perform histogram equalization on the given frequencies(freq) of the histogtam
    pdf=[]
    for x in freq:
        pdf.append(x/image_size)
    cdf = np.cumsum(pdf)
    new_level=[round(z*max_intensity) for z in cdf ]
    return new_level


def mapping (image,new_level,size): #replace the original value by the new computed levels and return new image
   new_image=image
   for i in range (size[0]):
            for j in range (size[1]):
                k=image[i,j]
                new_image[i,j]=new_level[k]
   return new_image


def Histogram_equalize(path,flag): #flag=0 for a grayscale and 1 for rgb
    im=cv2.imread(path,flag)
    
    if flag==0: #greyscale
        im=cv2.imread(path,0)
        
    elif flag==1:
        image=cv2.imread(path,1)
        im_gray=rgb2gray(cv2.cvtColor(image,cv2.COLOR_BGR2GRAY))
        im=cv2.convertScaleAbs(im_gray)
    
    frequency=Hist(im)
    new_level=Equalize(frequency,np.max(im),im.shape[0]*im.shape[1])
    new_image=mapping(im,new_level,[im.shape[0],im.shape[1]])
    return new_image
   
    

#main
new_rgb=Histogram_equalize("D:\SBME 3rd year\secomd term\CV\peppers.png",1)
rgb_grey=cv2.imread("D:\SBME 3rd year\secomd term\CV\peppers.png")
im_gray=rgb2gray(cv2.cvtColor(rgb_grey,cv2.COLOR_BGR2GRAY))
im=cv2.convertScaleAbs(im_gray)
res_rgb=np.hstack((new_rgb,im))
cv2.imshow("rgb",res_rgb)


new_grey=Histogram_equalize("D:\SBME 3rd year\secomd term\CV\lena_opencv_gray.jpg",0)
image_grey=cv2.imread("D:\SBME 3rd year\secomd term\CV\lena_opencv_gray.jpg",0)
res_grey=np.hstack((new_grey,image_grey))
cv2.imshow("grey",res_grey)

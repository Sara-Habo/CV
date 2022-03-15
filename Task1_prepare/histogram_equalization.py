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

def Equalize(freq,image_size): #perform histogram equalization on the given frequencies(freq) of the histogtam
    pdf=[]
    for x in freq:
        pdf.append(x/image_size)
    cdf = np.cumsum(pdf)
    new_level=[round(z*255) for z in cdf ]
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
        original_level=Hist(im)
        new_level=Equalize(original_level,im.shape[0]*im.shape[1])
        new_image=mapping(im,new_level,[im.shape[0],im.shape[1]])
   
    elif flag==1: #RGB image
        red=im[:,:,2]
        green=im[:,:,1]
        blue=im[:,:,0]
        new_image=im
       
        freq_r=Hist(red)
        freq_g=Hist(green)
        freq_b=Hist(blue)
        
        new_level_r=Equalize(freq_r,im.shape[0]*im.shape[1])
        new_level_g=Equalize(freq_g,im.shape[0]*im.shape[1])
        new_level_b=Equalize(freq_b,im.shape[0]*im.shape[1])
        
        new_r=mapping(red,new_level_r,[im.shape[0],im.shape[1]])
        new_image[:,:,2]=new_r
        
        new_g=mapping(green,new_level_g,[im.shape[0],im.shape[1]])
        new_image[:,:,1]=new_g
        
        new_b=mapping(blue,new_level_b,[im.shape[0],im.shape[1]])
        new_image[:,:,0]=new_b
    return new_image

#main
new_rgb=Histogram_equalize("D:\SBME 3rd year\secomd term\CV\peppers.png",1)
#cv2.imshow("new_image",new_rgb)
image_rgb=cv2.imread("D:\SBME 3rd year\secomd term\CV\peppers.png")
#cv2.imshow("original_rgb",image_rgb)

res_rgb = np.hstack((new_rgb,image_rgb))
# show image input vs output
cv2.imshow('rgb', res_rgb)

new_grey=Histogram_equalize("D:\SBME 3rd year\secomd term\CV\lena_opencv_gray.jpg",0)
image_grey=cv2.imread("D:\SBME 3rd year\secomd term\CV\lena_opencv_gray.jpg",0)
res_grey=np.hstack((new_grey,image_grey))
cv2.imshow("grey",res_grey)




        
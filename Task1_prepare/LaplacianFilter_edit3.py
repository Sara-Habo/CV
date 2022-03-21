import cv2
import numpy as np
from matplotlib import pyplot as plt
###LOF :laplacian of gaussian

def LOF(path):
    # loading image
    img_BGR = cv2.imread(path)
    # converting to gray scale
    img_gray = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2GRAY)
    # remove noise

    # One thing to note is that the Laplacian filter is a bit too sensitive. So,
    # it will work badly if there is noise in the image.
    # Hence we apply something known as a Gaussian Blur to smooth the image and make the Laplacian filter more effective.

    ########## parameter ##########
    ## source image
    ## Gaussian Kernel Size use (3,3)
    ## borderType
    img_G = cv2.GaussianBlur(img_gray, (3, 3), cv2.BORDER_CONSTANT)
    # apply laplacian filter
    ########## parameter ##########
    ## source img
    ## ddepth :change from format(like int,float ,...) to another format  actually change uint8 to 64float
    N_laplacian = cv2.Laplacian(img_G, cv2.CV_64F)  ##----> called negative laplacian
    P_laplacian = np.uint8(np.absolute(N_laplacian))  ##----> called positive laplacian
    #   negative      positive
    #   1   1  1     -1  -1  -1
    #   1  -4  1     -1   4  -1
    #   1   1  1     -1  -1  -1

    #Note number (4) is increase will make more sharpness

    print("N_laplacian ={}".format(N_laplacian))
    print("abs_laplacian ={}".format(np.absolute(N_laplacian)))
    print("P_laplacian ={}".format(P_laplacian))

    return img_gray,N_laplacian,P_laplacian

def LOF_RGB(path):
    img_BGR = cv2.imread(path)
    img_HSV = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)
    img_HSV_G = cv2.GaussianBlur(img_HSV[:,:,2], (3, 3), cv2.BORDER_CONSTANT)
    print(img_HSV_G.shape)
    img_HSV_Lap = cv2.Laplacian(img_HSV_G, cv2.CV_64F)
    img_HSV[:, :, 2]=img_HSV_Lap
    img_RGB_Lap = cv2.cvtColor(img_HSV,cv2.COLOR_HSV2RGB)
    return img_RGB_Lap


def FT_another_function(image):
    frequency = np.fft.fft2(image)
    fshift = np.fft.fftshift(frequency)
    return 20*np.log(np.abs(fshift))
def FFT(image):
    ft = np.fft.ifftshift(image)
    ft = np.fft.fft2(ft)
    return np.log(abs(np.fft.fftshift(ft)) + 1)



#img_gray,N_laplacian,P_laplacian=LOF("E:/temp third year second term/computer vision CV/Tasks/lena_opencv_gray.jpg")

img_filtered = LOF_RGB("E:/temp third year second term/computer vision CV/Tasks/laplacian_image_test.jpg")
plt.imshow(img_filtered)
plt.show()

# plt.subplot(231)
# plt.title("gray spacial")
# plt.imshow(img_gray,cmap = 'gray')
# plt.xticks([]), plt.yticks ([])
# plt.subplot(234)
# plt.title("gray frequency")
# plt.imshow(FFT(img_gray),cmap = 'gray')
# plt.xticks([]), plt.yticks ([])
# plt.subplot(232)
# plt.title("negative_lap special")
# plt.imshow(N_laplacian,cmap = 'gray')
# plt.xticks([]), plt.yticks ([])
# plt.subplot(235)
# plt.title("negative_lap frequency")
# plt.imshow(FFT(N_laplacian),cmap = 'gray')
# plt.xticks([]), plt.yticks ([])
# plt.subplot(233)
# plt.title("positive_lap special")
# plt.imshow(P_laplacian,cmap = 'gray')
# plt.xticks([]), plt.yticks ([])
# plt.subplot(236)
# plt.title("positive_lap frequency")
# plt.imshow(FFT(P_laplacian),cmap = 'gray')
# plt.xticks([]), plt.yticks ([])
# plt.show()

####refrence in order to benifit
#https://www.youtube.com/watch?v=t1xN7AFjp4o explain every thing
#https://www.youtube.com/watch?v=uNP6ZwQ3r6A  -->expalin concept
#https://www.youtube.com/watch?v=PxzaXOd_nHs  -->help in implement
#https://iq.opengenus.org/laplacian-filter/  -->useful article


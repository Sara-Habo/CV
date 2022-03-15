import cv2
import numpy as np
from matplotlib import pyplot as plt

# loading image
img_BGR = cv2.imread('E:/temp third year second term/computer vision CV/Tasks/laplacian_image_test.jpg')

# converting to gray scale
img_gray = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2GRAY)
print(img_gray)

# remove noise

#One thing to note is that the Laplacian filter is a bit too sensitive. So,
# it will work badly if there is noise in the image.
# Hence we apply something known as a Gaussian Blur to smooth the image and make the Laplacian filter more effective.

########## parameter ##########
## source image
## Gaussian Kernel Size use (3,3)
## borderType
img_G = cv2.GaussianBlur(img_gray,(3,3),cv2.BORDER_CONSTANT)


# apply laplacian filter
########## parameter ##########
## source img
## ddepth :change from format(like int,float ,...) to another format  actually change uint8 to 64float
N_laplacian = cv2.Laplacian(img_G,cv2.CV_64F)   ##----> called negative laplacian
P_laplacian = np.uint8(np.absolute(N_laplacian))          ##----> called positive laplacian
#   negative      positive
#   1   1  1     -1  -1  -1
#   1  -4  1     -1   4  -1
#   1   1  1     -1  -1  -1

plt.subplot(2,2,1),plt.imshow(img_gray,cmap = 'gray')
plt.title('Original')
plt.subplot(2,2,2),plt.imshow(img_G,cmap = 'gray')
plt.title('GaussianBlur')
plt.subplot(2,2,3),plt.imshow(N_laplacian,cmap = 'gray')
plt.title('negative laplacian')
plt.subplot(2,2,4),plt.imshow(P_laplacian,cmap = 'gray')
plt.title('positive laplacian')

plt.show()


####refrence in order to benifit
#https://www.youtube.com/watch?v=uNP6ZwQ3r6A  -->expalin concept
#https://www.youtube.com/watch?v=PxzaXOd_nHs  -->help in implement
#https://iq.opengenus.org/laplacian-filter/  -->useful article
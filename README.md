# CV
import cv2
from matplotlib import pyplot as plt
import numpy as np
img = cv2.imread("D:/habiba/biomedical 3/semester 2/cv/pic/022.png")

blur = cv2.blur(img,(5,5))

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original')
plt.xticks([]), plt.yticks ([])
plt.subplot(2,2,2),plt.imshow(blur,cmap = 'gray')
plt.title('blur')
plt.xticks([]), plt.yticks ([])

plt.show()

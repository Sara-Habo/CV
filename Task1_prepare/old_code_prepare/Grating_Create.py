import numpy as np
import matplotlib.pyplot as plt

################### creat 1D sine wave ###################
x = np.arange(-500,501 ,1)
wavelength = 200
y = np.sin((2 * np.pi * x)/wavelength)
plt.plot(x, y)
plt.show()
################### creat 2D sine wave ###################
X, Y = np.meshgrid(x, x) #creates a 2D representation that can be used as the basis for 2D equations
print ("X = {}".format(X))
print ("Y = {}".format(Y))
##oreinted along horizontal
grating = np.sin((2 * np.pi * X) /wavelength )
plt.set_cmap("gray")
plt.imshow(grating)
plt.show()
##oreinted along vertical
grating = np.sin((2 * np.pi * Y) /wavelength )
plt.set_cmap("gray")
plt.imshow(grating)
plt.show()
###oreinted with specific angle
angle = np.pi / 9##np.pi *1.75
grating =np.sin ((2 * np.pi *((X*np.cos(angle))+(Y*np.sin(angle)))) /wavelength)
plt.set_cmap("gray")
plt.imshow(grating)
plt.show()
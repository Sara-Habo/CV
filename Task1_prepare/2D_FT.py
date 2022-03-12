

import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(-500, 501, 1)

X, Y = np.meshgrid(x, x)

def function(wavelength, angle):
    # wavelength = 200
    #angle = 0
    grating = np.sin(
        2*np.pi*(X*np.cos(angle) + Y*np.sin(angle)) / wavelength
    )

    plt.set_cmap("gray")

    plt.subplot(131)
    plt.imshow(grating)

    # Calculate Fourier transform of grating without centralization
    ft = np.fft.ifft(grating)
    ft = np.fft.fft2(ft)
    ft = np.fft.fft(ft)

    plt.subplot(132)
    plt.imshow(abs(ft))
    #plt.imshow(math.log(abs(ft)+1,10))
    plt.xlim([0, 20]) # to zoom in effect frequency
    plt.ylim([20, 0])  # Note, order is reversed for y


    # Calculate Fourier transform of grating with centralization
    ft = np.fft.ifftshift(grating)
    ft = np.fft.fft2(ft)
    ft = np.fft.fftshift(ft)

    plt.subplot(133)
    plt.imshow(abs(ft))
    #plt.imshow(math.log(abs(ft)+1,10))
    plt.xlim([480, 520]) # to zoom in to the central part of the image
    plt.ylim([520,480])  # Note, that the limits on the y-axis are reversed. This is due to how Matplotlib deals with displaying images and axes.
    plt.show()
##############################main############################
function(200,0)

function(100,0)###decrease wavelength ----> increase frequency ------->increase distance between two dots

function(100,np.pi/9)
#distance of the dots from the centre represents the frequency of the sinusoidal grating
#orientation of the dots represents the orientation of the grating
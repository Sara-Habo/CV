# fourier_synthesis.py
import matplotlib.pyplot as plt
import numpy as np
image_filename = "Earth.png"
# # Read and process image
# image = plt.imread(image_filename)  ##image consist of RGB and alpha
# print(image.shape)
# image = image[:, :, :3].mean(axis=2)  # Convert to grayscale
#
# print(image.shape)
# plt.set_cmap("gray")
# plt.imshow(image)
# plt.axis("off")
# plt.show()

############### writing code as function ###################
def calculate_2Dft(image):
    ft = np.fft.ifftshift(image)
    ft = np.fft.fft2(ft)
    return  np.fft.fftshift(ft)
def calculate_I2Dft(FT):
    ift=np.fft.ifftshift(FT)
    ift=np.fft.ifft2(ift)
    ift=np.fft.fftshift(ift)
    return ift.real
image = plt.imread(image_filename)##read image
image = image[:,:,:3].mean(axis=2)##to get grayscale
FT = calculate_2Dft(image)
inverse_FT = calculate_I2Dft(FT)
plt.set_cmap("gray")
plt.subplot(231)
plt.title("gray image")
plt.imshow(image)
plt.subplot(232)
plt.title("FT image")
plt.imshow(abs(FT))
plt.subplot(233)
plt.title("using log without 1")
plt.imshow(np.log(abs(FT)))
plt.subplot(234)
plt.title("using log with 1")###  -----> to avoid problem log(0)
plt.imshow(np.log(abs(FT)+1))
plt.subplot(235)
plt.title("inverse FT of FT")
plt.imshow(inverse_FT)
plt.show()
################ big note to remember ################
# Now there are lots of dots that have non-zero values in the Fourier transform.
# Instead of five pairs of dots representing five sinusoidal gratings, you now have thousands of pairs of dots. This means that there are thousands of sinusoidal gratings present in the Earth image.
# Each pair of dots represents a sinusoidal grating with a specific frequency, amplitude, orientation, and phase. The further away the dots are from the centre, the higher the frequency.
# The brighter they are, the more prominent that grating is in the image as it has a higher amplitude.
# And the orientation of each pair of dots in relation to the centre represents the orientation of the gratings. The phase is also encoded in the Fourier transform.
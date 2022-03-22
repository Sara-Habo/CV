from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2gray
import cv2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 860)
        MainWindow.setStyleSheet("background-color: rgb(225, 221, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.spatial_domain = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.spatial_domain.setFont(font)
        self.spatial_domain.setObjectName("spatial_domain")
        self.horizontalLayout.addWidget(self.spatial_domain)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.original_image = QtWidgets.QLabel(self.centralwidget)
        self.original_image.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.original_image.setText("")
        self.original_image.setObjectName("original_image")
        self.verticalLayout_2.addWidget(self.original_image)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.filtered_image = QtWidgets.QLabel(self.centralwidget)
        self.filtered_image.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filtered_image.setText("")
        self.filtered_image.setObjectName("filtered_image")
        self.verticalLayout.addWidget(self.filtered_image)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frequency_domain = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.frequency_domain.setFont(font)
        self.frequency_domain.setObjectName("frequency_domain")
        self.horizontalLayout_2.addWidget(self.frequency_domain)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.original_freq = QtWidgets.QLabel(self.centralwidget)
        self.original_freq.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.original_freq.setText("")
        self.original_freq.setObjectName("original_freq")
        self.verticalLayout_3.addWidget(self.original_freq)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.filtered_freq = QtWidgets.QLabel(self.centralwidget)
        self.filtered_freq.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.filtered_freq.setText("")
        self.filtered_freq.setObjectName("filtered_freq")
        self.verticalLayout_4.addWidget(self.filtered_freq)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.filters = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.filters.setFont(font)
        self.filters.setObjectName("filters")
        self.horizontalLayout_3.addWidget(self.filters)
        self.choosefilter = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.choosefilter.setFont(font)
        self.choosefilter.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.choosefilter.setObjectName("choosefilter")
        self.choosefilter.addItem("")
        self.choosefilter.addItem("")
        self.choosefilter.addItem("")
        self.choosefilter.addItem("")
        self.choosefilter.addItem("")
        self.choosefilter.addItem("")
        self.choosefilter.addItem("")
        self.choosefilter.addItem("")
        self.choosefilter.addItem("")
        self.horizontalLayout_3.addWidget(self.choosefilter, 0, QtCore.Qt.AlignVCenter)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.original_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.original_label.setFont(font)
        self.original_label.setObjectName("original_label")
        self.horizontalLayout_4.addWidget(self.original_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.fltered_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fltered_label.setFont(font)
        self.fltered_label.setObjectName("fltered_label")
        self.horizontalLayout_4.addWidget(self.fltered_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_image = QtWidgets.QAction(MainWindow)
        self.actionOpen_image.setObjectName("actionOpen_image")
        self.menuFile.addAction(self.actionOpen_image)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.spatial_domain.setText(_translate("MainWindow", "Spatial domain:"))
        self.frequency_domain.setText(_translate("MainWindow", "Frequancy domain:"))
        self.filters.setText(_translate("MainWindow", "Filters :"))
        self.choosefilter.setItemText(0, _translate("MainWindow", "Choose filter"))
        self.choosefilter.setItemText(1, _translate("MainWindow", "High pass filter in frequancy"))
        self.choosefilter.setItemText(2, _translate("MainWindow", "High pass filter in spatial"))
        self.choosefilter.setItemText(3, _translate("MainWindow", "Low pass filter in frequancy"))
        self.choosefilter.setItemText(4, _translate("MainWindow", "Low pass filter in spatial"))
        self.choosefilter.setItemText(5, _translate("MainWindow", "Median filter"))
        self.choosefilter.setItemText(6, _translate("MainWindow", "Negative laplacian filter"))
        self.choosefilter.setItemText(7, _translate("MainWindow", "Positive laplacian filter"))
        self.choosefilter.setItemText(8, _translate("MainWindow", "Histogram Equalization"))
        self.original_label.setText(_translate("MainWindow", "Original"))
        self.fltered_label.setText(_translate("MainWindow", "Filtered"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_image.setText(_translate("MainWindow", "Open image"))




        self.actionOpen_image.triggered.connect(lambda:self.OpenImage())
        self.choosefilter.currentIndexChanged.connect(lambda : self.CheckComboBox())



    def OpenImage(self):
        self.filtered_image.clear()
        self.filtered_freq.clear()

        # browse an image and get its path
        fname=QFileDialog.getOpenFileName(None, 'Open file','D:\\', "Image files (*.png *.jpg *.gif *.jpeg)")
        self.imagePath = fname[0]

        #show original image
        self.original_img = QPixmap(self.imagePath)
        self.original_image.setPixmap(self.original_img)

        self.original_image.setScaledContents(True)
        self.original_image.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)

        # get gray scale image and show its spectrum in frequenncy domain
        self.imagee=plt.imread(self.imagePath)
        if len(self.imagee.shape)==2:
            self.im_gray=self.imagee
        else:
            self.im_gray=(cv2.cvtColor(self.imagee, cv2.COLOR_RGB2GRAY))

        plt.imsave("gray image.png", self.im_gray, cmap="gray")
        self.original_frequency=self.FFT(self.im_gray)
        plt.imsave("Original in Freq.png", self.original_frequency,cmap="gray")
        self.original_frequency = QPixmap("Original in Freq.png")
        self.original_freq.setPixmap(self.original_frequency)
        self.original_freq.setScaledContents(True)
        self.original_freq.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

        if self.choosefilter.currentText() == "Choose filter":
            self.filtered_image.setFont(QFont("Arial", 15))
            self.filtered_image.setText("Please choose filter from the combobox")
        self.CheckComboBox()

    def CheckComboBox(self):

        if len(self.imagee.shape) == 2:
            flag = 0
        else:
            flag = 1

        self.filtered_image.clear()
        self.filtered_freq.clear()
        if self.choosefilter.currentText() == "Choose filter":
            self.filtered_image.setFont(QFont("Arial", 15))
            self.filtered_image.setText("Please choose filter from the combobox")

        elif self.choosefilter.currentText() == "Histogram Equalization":
            self.original_img = QPixmap("gray image.png")
            self.original_image.setPixmap(self.original_img)

            self.original_image.setScaledContents( True)
            self.original_image.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

            if len(self.imagee.shape) == 2:
                print("if")
                self.equalized_image = self.Histogram_equalize(self.imagePath, 0)
                self.ShowFilteredImage(self.equalized_image)
            else:
                print("else")
                self.equalized_image=self.Histogram_equalize(self.imagePath, 1)
                self.ShowFilteredImage(self.equalized_image)
            self.ShowFilteredInFrequency(self.equalized_image, 0)
            print("filtered in domain")

        elif self.choosefilter.currentText() == "Negative laplacian filter":
            if len(self.imagee.shape) == 2:
                self.N_laplacianImage = self.LOF_gray(self.imagePath, 0)
                self.ShowFilteredImage(self.N_laplacianImage)
                self.ShowFilteredInFrequency(self.N_laplacianImage, 0)
            else:
                self.N_laplacianImage = self.LOF_RGB(self.imagePath)
                self.ShowFilteredImage(self.N_laplacianImage)
                self.ShowFilteredInFrequency(self.N_laplacianImage, 1)

        elif self.choosefilter.currentText() == "Positive laplacian filter":
            if len(self.imagee.shape) == 2:
                self.P_laplacianImage = self.LOF_gray(self.imagePath, 1)
                self.ShowFilteredImage(self.P_laplacianImage)
                self.ShowFilteredInFrequency(self.P_laplacianImage, 0)
            else:
                self.P_laplacianImage = self.LOF_RGB(self.imagePath)
                self.ShowFilteredImage(self.P_laplacianImage)
                self.ShowFilteredInFrequency(self.P_laplacianImage, 1)
        elif self.choosefilter.currentText() == "Median filter":
            if len(self.imagee.shape) == 2:
                self.median_filteredimage = self.median_filter(self.imagePath, 0)

            else:
                self.median_filteredimage = self.median_filter(self.imagePath, 1)
            self.ShowFilteredImage(self.median_filteredimage)
            self.ShowFilteredInFrequency(self.median_filteredimage, 1)
        elif self.choosefilter.currentText() == "Low pass filter in spatial":
            self.lowfilter_spatial = self.low_filter_spatial(self.imagePath)
            self.ShowFilteredImage(self.lowfilter_spatial)
            self.ShowFilteredInFrequency(self.lowfilter_spatial, 1)

        elif self.choosefilter.currentText() == "High pass filter in spatial":
            self.sharp_images = self.High_filter_spatial(self.imagePath,flag)
            self.ShowFilteredImage(self.sharp_images)
            self.ShowFilteredInFrequency(self.sharp_images, flag)

        elif self.choosefilter.currentText() == "High pass filter in frequancy":
            self.sharp_images = self.High_filter_frequency(self.imagePath,flag)
            self.ShowFilteredImage(self.sharp_images)
            self.ShowFilteredInFrequency(self.sharp_images, flag)

    def High_filter_frequency(self, imagePath, flag):

        self.image = plt.imread(imagePath)

        if flag == 0:
            self.image = self.High_filter_for_component(self.image)
        else:
            for i in range(3):
                component = self.image[:, :, i]
                self.image[:, :, i] = self.High_filter_for_component(component)
        return self.image

    def High_filter_for_component(self, img):
        #  Fourier transform
        fimg = np.fft.fft2(img)
        fshift = np.fft.fftshift(fimg)

        #  Set the high pass filter
        rows = img.shape[0]
        cols = img.shape[1]
        crow, ccol = int(rows / 2), int(cols / 2)
        fshift[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0

        #  Inverse Fourier transform
        ishift = np.fft.ifftshift(fshift)
        iimg = np.fft.ifft2(ishift)
        iimg = np.abs(iimg)
        return iimg

    def High_filter_spatial(self, imagePath, flag):
        self.image = plt.imread(imagePath)
        kernel = np.array([[-1, -1, -1],
                           [-1, 8, -1],
                           [-1, -1, -1]])
        if flag == 0:
            self.image_sharp = cv2.filter2D(src=self.image, ddepth=-1, kernel=kernel)

        else:
            self.RGB_image = self.image
            self.RGB_image[:, :, 0] = cv2.filter2D(src= self.RGB_image[:, :, 0], ddepth=-1, kernel=kernel)
            self.RGB_image[:, :, 1] = cv2.filter2D(src= self.RGB_image[:, :, 1], ddepth=-1, kernel=kernel)
            self.RGB_image[:, :, 2] = cv2.filter2D(src= self.RGB_image[:, :, 2], ddepth=-1, kernel=kernel)
            self.image_sharp = self.RGB_image

        return self.image_sharp

    def low_filter_spatial(self, image_path):
        self.image = cv2.imread(image_path)
        self.blurimage = cv2.blur(self.image, (5, 5))
        self.blurimage = cv2.cvtColor(self.blurimage, cv2.COLOR_BGR2RGB)

        return self.blurimage

    def lowPassFiltering(self, img, size):
        h, w = img.shape[0:2]
        h1, w1 = int(h / 2), int(w / 2)
        img2 = np.zeros((h, w),
                        np.uint8)
        img2[h1 - int(size / 2):h1 + int(size / 2), w1 - int(size / 2):w1 + int(
            size / 2)] = 1
        img3 = img2 * img
        return img3

    def frq_filter(self, file_path, flag=1):

        # read pic
        gray = cv2.imread(file_path)
        gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
        h, w = gray.shape

        # Fourier transform
        img_dft = np.fft.fft2(gray)
        dft_shift = np.fft.fftshift(img_dft)  # Move frequency domain from upper left to middle

        # Low-pass filter
        dft_shift = self.lowPassFiltering(dft_shift, 100)

        # Inverse Fourier Transform
        idft_shift = np.fft.ifftshift(dft_shift)  # Move the frequency domain from the middle to the upper left corner
        ifimg = np.fft.ifft2(idft_shift)  # Fourier library function call
        ifimg = np.abs(ifimg)
        # cv2.imshow("ifimg", np.int8(ifimg))
        # cv2.imshow("gray", gray)
        plt.imsave("filtered image.png", ifimg, cmap="gray")
        self.filtered_img = QPixmap("filtered image.png")
        self.filtered_image.setPixmap(self.filtered_img)
        img_dft = np.fft.fft2(ifimg)
        dft_shift = np.fft.fftshift(img_dft)
        res = np.log(np.abs(dft_shift))
        plt.imsave("filtered in Freq.png", res, cmap="gray")
        self.filtered_frequency = QPixmap("filtered in Freq.png")
        self.filtered_freq.setPixmap(self.filtered_frequency)

    def median_filter(self, image, color_flag):
        self.im_arr = cv2.imread(image)
        if color_flag == 0:
            self.median = cv2.medianBlur(self.im_arr, 3)
        else:
            self.median = self.im_arr
            self.median[:, :, 0] = cv2.medianBlur(self.im_arr[:, :, 0], 5)
            self.median[:, :, 1] = cv2.medianBlur(self.im_arr[:, :, 1], 5)
            self.median[:, :, 2] = cv2.medianBlur(self.im_arr[:, :, 2], 5)
            self.median = cv2.cvtColor(self.median, cv2.COLOR_BGR2RGB)

        return self.median

    def ShowFilteredImage(self, image):

        plt.imsave("filtered image.png",image,cmap="gray")
        self.filtered_img=QPixmap("filtered image.png")

        self.filtered_image.setPixmap(self.filtered_img)
        self.filtered_image.setScaledContents(True)
        self.filtered_image.setSizePolicy(QSizePolicy.Ignored,QSizePolicy.Ignored)

    def ShowFilteredInFrequency(self,image,gray_RGB_flag):
        self.filtered_freq.clear()
        if gray_RGB_flag == 1: ##that mean if flag ==1  image is rgb and need to convert to gary to get frequency domain
            image = (cv2.cvtColor(image, cv2.COLOR_RGB2GRAY))
        self.filtered_frequency=self.FFT(image)
        plt.imsave("filtered in Freq.png", self.filtered_frequency, cmap="gray")

        self.filtered_frequency = QPixmap("filtered in Freq.png")
        self.filtered_freq.setPixmap(self.filtered_frequency)

        self.filtered_freq.setScaledContents(True)
        self.filtered_freq.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

    def LOF_gray(self, path, N_P_flag):
        self.img_BGR = cv2.imread(path)
        self.img_gray = cv2.cvtColor(self.img_BGR, cv2.COLOR_BGR2GRAY)
        self.img_G = cv2.GaussianBlur(self.img_gray, (3, 3), cv2.BORDER_CONSTANT)
        self.N_laplacian = cv2.Laplacian(self.img_G, cv2.CV_64F)
        self.P_laplacian = np.uint8(np.absolute(self.N_laplacian))
        if N_P_flag == 0:
            return self.N_laplacian
        else:
            return self.P_laplacian

    def LOF_RGB(self, path):
        self.img_BGR = cv2.imread(path)
        self.img_HSV = cv2.cvtColor(self.img_BGR, cv2.COLOR_BGR2HSV)
        self.img_HSV_G = cv2.GaussianBlur(self.img_HSV[:, :, 2], (3, 3), cv2.BORDER_CONSTANT)
        self.img_HSV[:, :, 2] = cv2.Laplacian(self.img_HSV_G, cv2.CV_64F)
        self.img_HSV_RGB = cv2.cvtColor(self.img_HSV, cv2.COLOR_HSV2RGB)
        return self.img_HSV_RGB

    def FFT(self, image):
        self.ft = np.fft.ifftshift(image)
        self.ft = np.fft.fft2(self.ft)
        return np.log(abs(np.fft.fftshift(self.ft)) + 1)

    def Hist(self, image):  #return the image histogram
        print("in hist")
        self.h = np.zeros(shape=(1,256),dtype=int)
        self.s = image.shape
        print("after shape")
        for i in range(self.s[0]):
            for j in range(self.s[1]):
                k = image[i, j]
                self.h[0, k] = self.h[0, k]+1
        return self.h[0]

    def Equalize(self, freq, max_intensity, image_size): #perform histogram equalization on the given frequencies(freq) of the histogtam
        self.pdf = []
        for x in freq:
            self.pdf.append(x/image_size)
        self.cdf = np.cumsum(self.pdf)
        self.new_level=[round(z*max_intensity) for z in self.cdf ]
        return self.new_level

    def mapping (self, image, new_level, size): #replace the original value by the new computed levels and return new image
       self.new_image = image
       for i in range (size[0]):
                for j in range (size[1]):
                    k = image[i, j]
                    self.new_image[i, j] = self.new_level[k]
       return self.new_image

    def Histogram_equalize(self,path,flag): #flag=0 for a grayscale and 1 for rgb

        if flag == 0:  #greyscale
            self.im = self.imagee

        elif flag == 1:
            self.im=self.im_gray

        self.frequency = self.Hist(self.im)
        print("f")
        self.new_level = self.Equalize(self.frequency, np.max(self.im), self.im.shape[0]*self.im.shape[1])
        print("e")
        self.equalized_image = self.mapping(self.im, self.new_level, [self.im.shape[0], self.im.shape[1]])
        print("m")
        return self.equalized_image

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
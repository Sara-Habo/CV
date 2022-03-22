# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task1_final.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

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
        MainWindow.setStyleSheet("QMainWindow {background-image:url(9.jpg);};")

        MainWindow.resize(1093, 796)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_program = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.title_program.setMaximumSize(QtCore.QSize(16777215, 200))
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.title_program.setFont(font)
        self.title_program.setStyleSheet("QLabel {  color : white; }\");")
        self.title_program.setAlignment(QtCore.Qt.AlignCenter)
        self.title_program.setObjectName("title_program")
        self.verticalLayout.addWidget(self.title_program)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.original_image = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.original_image.setStyleSheet("")
        self.original_image.setText("")
        self.original_image.setObjectName("original_image")
        self.verticalLayout_3.addWidget(self.original_image)
        self.original_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.original_label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.original_label.setFont(font)
        self.original_label.setStyleSheet("QLabel {  color : white; }\");")
        self.original_label.setAlignment(QtCore.Qt.AlignCenter)
        self.original_label.setObjectName("original_label")
        self.verticalLayout_3.addWidget(self.original_label)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.filtered_image = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.filtered_image.setStyleSheet("")
        self.filtered_image.setText("")
        self.filtered_image.setObjectName("filtered_image")
        self.verticalLayout_4.addWidget(self.filtered_image)
        self.filtered_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.filtered_label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.filtered_label.setFont(font)
        self.filtered_label.setStyleSheet("QLabel {  color : white; }\");")
        self.filtered_label.setAlignment(QtCore.Qt.AlignCenter)
        self.filtered_label.setObjectName("filtered_label")
        self.verticalLayout_4.addWidget(self.filtered_label)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.original_freq = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.original_freq.setStyleSheet("")
        self.original_freq.setText("")
        self.original_freq.setObjectName("original_freq")
        self.verticalLayout_5.addWidget(self.original_freq)
        self.original_label_freq = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.original_label_freq.setMaximumSize(QtCore.QSize(1000, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.original_label_freq.setFont(font)
        self.original_label_freq.setStyleSheet("QLabel {  color : white; }\");")
        self.original_label_freq.setAlignment(QtCore.Qt.AlignCenter)
        self.original_label_freq.setObjectName("original_label_freq")
        self.verticalLayout_5.addWidget(self.original_label_freq)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.filtered_freq = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.filtered_freq.setStyleSheet("")
        self.filtered_freq.setText("")
        self.filtered_freq.setObjectName("filtered_freq")
        self.verticalLayout_6.addWidget(self.filtered_freq)
        self.filtered_label_freq = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.filtered_label_freq.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.filtered_label_freq.setFont(font)
        self.filtered_label_freq.setStyleSheet("QLabel {  color : white; }\");")
        self.filtered_label_freq.setAlignment(QtCore.Qt.AlignCenter)
        self.filtered_label_freq.setObjectName("filtered_label_freq")
        self.verticalLayout_6.addWidget(self.filtered_label_freq)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.title_setting = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.title_setting.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.title_setting.setFont(font)
        self.title_setting.setStyleSheet("QLabel {  color : white; }\");")
        self.title_setting.setAlignment(QtCore.Qt.AlignCenter)
        self.title_setting.setObjectName("title_setting")
        self.verticalLayout_7.addWidget(self.title_setting)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
        self.open_image = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.open_image.setFont(font)
        self.open_image.setStyleSheet("QPushButton {  color : black;  }\");")
        self.open_image.setObjectName("open_image")
        self.verticalLayout_8.addWidget(self.open_image)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_8.addItem(spacerItem1)
        self.choosefilter = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.choosefilter.setFont(font)
        self.choosefilter.setStyleSheet("QComboBox {  color : black;}\");")
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
        self.verticalLayout_8.addWidget(self.choosefilter)
        self.warning = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.warning.setFont(font)
        self.warning.setStyleSheet("QLabel {  color : RED; }\");")
        self.warning.setObjectName("warning")
        self.verticalLayout_8.addWidget(self.warning)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem2)
        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1093, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_program.setText(_translate("MainWindow", "Image editor"))
        self.original_label.setText(_translate("MainWindow", "The original image in spatial"))
        self.filtered_label.setText(_translate("MainWindow", "The filtered image in spatial"))
        self.original_label_freq.setText(_translate("MainWindow", "The original image in frequency"))
        self.filtered_label_freq.setText(_translate("MainWindow", "The filtered image in frequency"))
        self.title_setting.setText(_translate("MainWindow", "Editor setting"))
        self.open_image.setText(_translate("MainWindow", "Choose image"))
        self.choosefilter.setItemText(0, _translate("MainWindow", "Choose filter"))
        self.choosefilter.setItemText(1, _translate("MainWindow", "High pass filter in frequancy"))
        self.choosefilter.setItemText(2, _translate("MainWindow", "High pass filter in spatial"))
        self.choosefilter.setItemText(3, _translate("MainWindow", "Low pass filter in frequancy"))
        self.choosefilter.setItemText(4, _translate("MainWindow", "Low pass filter in spatial"))
        self.choosefilter.setItemText(5, _translate("MainWindow", "Median filter"))
        self.choosefilter.setItemText(6, _translate("MainWindow", "Negative laplacian filter"))
        self.choosefilter.setItemText(7, _translate("MainWindow", "Positive laplacian filter"))
        self.choosefilter.setItemText(8, _translate("MainWindow", "Histogram Equalization"))
        self.warning.setText(_translate("MainWindow", "*Please choose the image first "))
        # ------------------------------------setting-------------------------------------
        self.original_label.hide()
        self.filtered_label.hide()
        self.original_label_freq.hide()
        self.filtered_label_freq.hide()
        self.warning.hide()

        # ---------------------------------functions----------------------------------------
        self.open_image.clicked.connect(lambda: self.OpenImage())
        self.choosefilter.currentIndexChanged.connect(lambda: self.CheckComboBox())

    open_flag = 0
    def OpenImage(self):
        self.filtered_image.clear()
        self.filtered_freq.clear()
        self.original_label.show()
        self.original_label_freq.show()
        self.open_flag = 1

        # browse an image and get its path
        fname = QFileDialog.getOpenFileName(None, 'Open file', 'D:\\', "Image files (*.png *.jpg *.gif *.jpeg)")
        self.imagePath = fname[0]

        # show original image
        self.original_img = QPixmap(self.imagePath)
        self.original_image.setPixmap(self.original_img)

        self.original_image.setScaledContents(True)
        self.original_image.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

        # get gray scale image and show its spectrum in frequenncy domain
        self.imagee = plt.imread(self.imagePath)
        if len(self.imagee.shape) == 2:
            self.im_gray = self.imagee
        else:
            self.im_gray = (cv2.cvtColor(self.imagee, cv2.COLOR_RGB2GRAY))

        plt.imsave("gray image.png", self.im_gray, cmap="gray")
        self.original_frequency = self.FFT(self.im_gray)
        plt.imsave("Original in Freq.png", self.original_frequency, cmap="gray")
        self.original_frequency = QPixmap("Original in Freq.png")
        self.original_freq.setPixmap(self.original_frequency)
        self.original_freq.setScaledContents(True)
        self.original_freq.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

        if self.choosefilter.currentText() == "Choose filter":
            self.filtered_image.setFont(QFont("Arial", 15))
            self.filtered_image.setText("Please choose filter from the combobox")

        self.CheckComboBox()

    def CheckComboBox(self):
        if self.open_flag == 0:
            self.warning.show()
        else:
            self.warning.hide()
            if len(self.imagee.shape) == 2:
                flag = 0
            else:
                flag = 1

            self.filtered_image.clear()
            self.filtered_freq.clear()
            self.filtered_label.show()
            self.filtered_label_freq.show()

            if self.choosefilter.currentText() == "Choose filter":
                self.filtered_image.setFont(QFont("Arial", 15))
                self.warning.show()
                self.warning.setText("Please choose filter from the combobox")

            elif self.choosefilter.currentText() == "Histogram Equalization":
                self.original_img = QPixmap("gray image.png")
                self.original_image.setPixmap(self.original_img)

                self.original_image.setScaledContents(True)
                self.original_image.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

                if len(self.imagee.shape) == 2:
                    self.equalized_image = self.Histogram_equalize(self.imagePath, 0)
                    self.ShowFilteredImage(self.equalized_image)
                else:
                    self.equalized_image = self.Histogram_equalize(self.imagePath, 1)
                    self.ShowFilteredImage(self.equalized_image)
                self.ShowFilteredInFrequency(self.equalized_image, 0)

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
                
            elif self.choosefilter.currentText() == "Low pass filter in frequancy":
                self.smooth_image = self.frq_filter(self.imagePath,flag)
                print("filter done")
                self.ShowFilteredImage(self.smooth_image)
                self.ShowFilteredInFrequency(self.smooth_image, flag)
                
            elif self.choosefilter.currentText() == "High pass filter in spatial":
                self.sharp_images = self.High_filter_spatial(self.imagePath, flag)
                self.ShowFilteredImage(self.sharp_images)
                self.ShowFilteredInFrequency(self.sharp_images, flag)

            elif self.choosefilter.currentText() == "High pass filter in frequancy":
                self.sharp_images = self.High_filter_frequency(self.imagePath, flag)
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
            self.RGB_image[:, :, 0] = cv2.filter2D(src=self.RGB_image[:, :, 0], ddepth=-1, kernel=kernel)
            self.RGB_image[:, :, 1] = cv2.filter2D(src=self.RGB_image[:, :, 1], ddepth=-1, kernel=kernel)
            self.RGB_image[:, :, 2] = cv2.filter2D(src=self.RGB_image[:, :, 2], ddepth=-1, kernel=kernel)
            self.image_sharp = self.RGB_image

        return self.image_sharp

    def low_filter_spatial(self, image_path):
        self.image = cv2.imread(image_path)
        self.blurimage = cv2.blur(self.image, (5, 5))
        self.blurimage = cv2.cvtColor(self.blurimage, cv2.COLOR_BGR2RGB)

        return self.blurimage

   
    def low_filter_for_component(self,img):

        # Fourier transform
        img_dft = np.fft.fft2(img)
        dft_shift = np.fft.fftshift(img_dft)  # Move frequency domain from upper left to middle

        # Low-pass filter
        h = dft_shift.shape[0]
        w = dft_shift.shape[1]
        h_center, w_center = int(h / 2), int(w / 2)
        img2 = np.zeros((h, w),np.uint8)
        img2[h_center - 50 : h_center + 50, w_center - 50: w_center + 50] = 1
        dft_shift = img2 * dft_shift

        # Inverse Fourier Transform
        inverse_dft_shift = np.fft.ifftshift(dft_shift)  # Move the frequency domain from the middle to the upper left corner
        inverse_fimg = np.fft.ifft2(inverse_dft_shift)  # Fourier library function call
        inverse_fimg = np.abs(inverse_fimg)

        return inverse_fimg

    def frq_filter(self, file_path, flag):

        # read pic
        self.image = plt.imread(file_path)

        if flag == 0:
            self.image = self.low_filter_for_component(self.image)
        else:
            for i in range(3):
                component = self.image[:, :, i]
                self.image[:, :, i] = self.low_filter_for_component(component)
        return self.image


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

        plt.imsave("filtered image.png", image, cmap="gray")
        self.filtered_img = QPixmap("filtered image.png")

        self.filtered_image.setPixmap(self.filtered_img)
        self.filtered_image.setScaledContents(True)
        self.filtered_image.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

    def ShowFilteredInFrequency(self, image, gray_RGB_flag):
        self.filtered_freq.clear()
        if gray_RGB_flag == 1:  ##that mean if flag ==1  image is rgb and need to convert to gary to get frequency domain
            image = (cv2.cvtColor(image, cv2.COLOR_RGB2GRAY))
        self.filtered_frequency = self.FFT(image)
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
        self.f = np.fft.fft2(image)
        self.fshift = np.fft.fftshift(self.f)
        self.magnitude_spectrum = np.abs(self.fshift)  # abs is equivalent to Norm-2 L2
        self.magnitude_spectrum_log_clear = np.log(self.magnitude_spectrum + 1)
        return self.magnitude_spectrum_log_clear

    def Hist(self, image):  # return the image histogram
        self.h = np.zeros(shape=(1, 256), dtype=int)
        self.s = image.shape
        for i in range(self.s[0]):
            for j in range(self.s[1]):
                k = image[i, j]
                self.h[0, k] = self.h[0, k] + 1
        return self.h[0]

    def Equalize(self, freq, max_intensity,
                 image_size):  # perform histogram equalization on the given frequencies(freq) of the histogtam
        self.pdf = []
        for x in freq:
            self.pdf.append(x / image_size)
        self.cdf = np.cumsum(self.pdf)
        self.new_level = [round(z * max_intensity) for z in self.cdf]
        return self.new_level

    def mapping(self, image, new_level,
                size):  # replace the original value by the new computed levels and return new image
        self.new_image = image
        for i in range(size[0]):
            for j in range(size[1]):
                k = image[i, j]
                self.new_image[i, j] = self.new_level[k]
        return self.new_image

    def Histogram_equalize(self, path, flag):  # flag=0 for a grayscale and 1 for rgb

        if flag == 0:  # greyscale
            self.im = self.imagee

        elif flag == 1:
            self.im = self.im_gray

        self.frequency = self.Hist(self.im)
        self.new_level = self.Equalize(self.frequency, np.max(self.im), self.im.shape[0] * self.im.shape[1])
        self.equalized_image = self.mapping(self.im, self.new_level, [self.im.shape[0], self.im.shape[1]])
        return self.equalized_image


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


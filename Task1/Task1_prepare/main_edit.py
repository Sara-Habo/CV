# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
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
        MainWindow.resize(800, 860)
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
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.original = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.original.setFont(font)
        self.original.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.original.setTextFormat(QtCore.Qt.PlainText)
        self.original.setObjectName("original")
        self.verticalLayout_2.addWidget(self.original, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignLeft)
        self.original_image = QtWidgets.QLabel(self.centralwidget)
        self.original_image.setText("")
        self.original_image.setObjectName("original_image")
        self.verticalLayout_2.addWidget(self.original_image)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.filtered = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.filtered.setFont(font)
        self.filtered.setObjectName("filtered")
        self.verticalLayout.addWidget(self.filtered, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignLeft)
        self.filtered_image = QtWidgets.QLabel(self.centralwidget)
        self.filtered_image.setText("")
        self.filtered_image.setObjectName("filtered_image")
        self.verticalLayout.addWidget(self.filtered_image)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
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
        self.original_freq.setText("")
        self.original_freq.setObjectName("original_freq")
        self.verticalLayout_3.addWidget(self.original_freq)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.filtered_freq = QtWidgets.QLabel(self.centralwidget)
        self.filtered_freq.setText("")
        self.filtered_freq.setObjectName("filtered_freq")
        self.verticalLayout_4.addWidget(self.filtered_freq)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
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
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
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
        font = QtGui.QFont()
        font.setPointSize(9)
        self.actionOpen_image.setFont(font)
        self.actionOpen_image.setObjectName("actionOpen_image")
        self.menuFile.addAction(self.actionOpen_image)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.spatial_domain.setText(_translate("MainWindow", "Spatial domain:"))
        self.original.setText(_translate("MainWindow", "Original"))
        self.filtered.setText(_translate("MainWindow", "Filtered"))
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
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_image.setText(_translate("MainWindow", "Open image"))



        self.actionOpen_image.triggered.connect(lambda:self.OpenImage())
        self.choosefilter.currentIndexChanged.connect(lambda : self.CheckComboBox())


    def OpenImage(self):
        # browse an image and get its path
        fname=QFileDialog.getOpenFileName(None, 'Open file','D:\\', "Image files (*.jpg *.gif)")
        imagePath = fname[0]
        #show original image
        self.original_img = QPixmap(imagePath)
        self.original_image.setPixmap(self.original_img)
        # get gray scale image and show its spectrum in frequenncy domain
        self.imagee=cv2.imread(imagePath)
        self.im_gray=rgb2gray(cv2.cvtColor(self.imagee,cv2.COLOR_BGR2RGB))
        self.original_frequency=self.FFT(self.im_gray)
        plt.imsave("Original in Freq.png",self.original_frequency,cmap="gray")
        self.original_frequency = QPixmap("Original in Freq.png")
        self.original_freq.setPixmap(self.original_frequency)

        if self.choosefilter.currentText()=="Choose filter":
            self.filtered_image.setFont(QFont("Arial",15))
            self.filtered_image.setText("Please choose filter from the combobox")

    def CheckComboBox(self):
        if self.choosefilter.currentText()=="Choose filter":
            self.filtered_image.setFont(QFont("Arial",15))
            self.filtered_image.setText("Please choose filter from the combobox")
        





    def FFT(self,image):
        self.ft = np.fft.ifftshift(image)
        self.ft = np.fft.fft2(self.ft)
        return np.log(abs(np.fft.fftshift(self.ft)) + 1)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


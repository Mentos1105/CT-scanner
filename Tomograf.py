# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI project.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import datetime
import tempfile
from PyQt5 import QtCore, QtGui, QtWidgets
from skimage import io, color
from skimage.transform import rescale, resize
from skimage.filters import gaussian
from math import pi, radians, cos, sin, ceil
import numpy as np
import sys
import pydicom
import matplotlib.pyplot as plt
from pydicom.dataset import Dataset, FileDataset


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(916, 585)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(400, 510, 75, 23))
        self.startButton.setObjectName("startButton")
        self.startButton.clicked.connect(self.startProcessing)
        self.chooseImageButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseImageButton.setGeometry(QtCore.QRect(170, 300, 75, 23))
        self.chooseImageButton.setObjectName("chooseImageButton")
        self.inputImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.inputImageLabel.setGeometry(QtCore.QRect(130, 40, 81, 16))
        self.inputImageLabel.setObjectName("inputImageLabel")
        self.sinogramLabel = QtWidgets.QLabel(self.centralwidget)
        self.sinogramLabel.setGeometry(QtCore.QRect(440, 40, 51, 16))
        self.sinogramLabel.setObjectName("sinogramLabel")
        self.outputImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputImageLabel.setGeometry(QtCore.QRect(710, 40, 81, 16))
        self.outputImageLabel.setObjectName("outputImageLabel")
        self.inputImage = QtWidgets.QLabel(self.centralwidget)
        self.inputImage.setGeometry(QtCore.QRect(50, 80, 251, 191))
        self.inputImage.setFrameShape(QtWidgets.QFrame.Box)
        self.inputImage.setText("")
        self.inputImage.setObjectName("inputImage")
        self.sinogram = QtWidgets.QLabel(self.centralwidget)
        self.sinogram.setGeometry(QtCore.QRect(340, 80, 251, 191))
        self.sinogram.setFrameShape(QtWidgets.QFrame.Box)
        self.sinogram.setText("")
        self.sinogram.setObjectName("sinogram")
        self.outputImage = QtWidgets.QLabel(self.centralwidget)
        self.outputImage.setGeometry(QtCore.QRect(630, 80, 251, 191))
        self.outputImage.setFrameShape(QtWidgets.QFrame.Box)
        self.outputImage.setText("")
        self.outputImage.setObjectName("outputImage")
        self.progressSlider = QtWidgets.QSlider(self.centralwidget)
        self.progressSlider.setGeometry(QtCore.QRect(170, 460, 111, 22))
        self.progressSlider.setOrientation(QtCore.Qt.Horizontal)
        self.progressSlider.setObjectName("progressSlider")
        self.chooseImageLabel = QtWidgets.QLabel(self.centralwidget)
        self.chooseImageLabel.setGeometry(QtCore.QRect(60, 300, 81, 21))
        self.chooseImageLabel.setObjectName("chooseImageLabel")
        self.alphaStepTextfield = QtWidgets.QLineEdit(self.centralwidget)
        self.alphaStepTextfield.setGeometry(QtCore.QRect(170, 340, 113, 20))
        self.alphaStepTextfield.setObjectName("alphaStepTextfield")
        self.alphaStepTextfield.setText("1")
        self.numOfDetectorsTextfield = QtWidgets.QLineEdit(self.centralwidget)
        self.numOfDetectorsTextfield.setGeometry(QtCore.QRect(170, 370, 113, 20))
        self.numOfDetectorsTextfield.setObjectName("numOfDetectorsTextfield")
        self.numOfDetectorsTextfield.setText("180")
        self.angularRangeTextfield = QtWidgets.QLineEdit(self.centralwidget)
        self.angularRangeTextfield.setGeometry(QtCore.QRect(170, 400, 113, 20))
        self.angularRangeTextfield.setObjectName("angularRangeTextfield")
        self.angularRangeTextfield.setText("180")
        self.alphaStepLabel = QtWidgets.QLabel(self.centralwidget)
        self.alphaStepLabel.setGeometry(QtCore.QRect(60, 340, 81, 16))
        self.alphaStepLabel.setObjectName("alphaStepLabel")
        self.numOfDetectorsLabel = QtWidgets.QLabel(self.centralwidget)
        self.numOfDetectorsLabel.setGeometry(QtCore.QRect(60, 370, 91, 16))
        self.numOfDetectorsLabel.setObjectName("numOfDetectorsLabel")
        self.angularRangeLabel = QtWidgets.QLabel(self.centralwidget)
        self.angularRangeLabel.setGeometry(QtCore.QRect(60, 400, 101, 16))
        self.angularRangeLabel.setObjectName("angularRangeLabel")
        self.progressLabel = QtWidgets.QLabel(self.centralwidget)
        self.progressLabel.setGeometry(QtCore.QRect(60, 460, 47, 13))
        self.progressLabel.setObjectName("progressLabel")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(620, 380, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.filterCheckbox = QtWidgets.QCheckBox(self.centralwidget)
        self.filterCheckbox.setGeometry(QtCore.QRect(170, 430, 70, 17))
        self.filterCheckbox.setObjectName("filterCheckbox")
        self.commentsTextField = QtWidgets.QTextEdit(self.centralwidget)
        self.commentsTextField.setGeometry(QtCore.QRect(620, 420, 251, 71))
        self.commentsTextField.setObjectName("commentsTextField")
        self.patientNameTextfield = QtWidgets.QTextEdit(self.centralwidget)
        self.patientNameTextfield.setGeometry(QtCore.QRect(620, 290, 251, 71))
        self.patientNameTextfield.setObjectName("patientNameTextfield")
        self.patientNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.patientNameLabel.setGeometry(QtCore.QRect(476, 320, 111, 20))
        self.patientNameLabel.setObjectName("patientNameLabel")
        self.examinationDateLabel = QtWidgets.QLabel(self.centralwidget)
        self.examinationDateLabel.setGeometry(QtCore.QRect(480, 380, 71, 16))
        self.examinationDateLabel.setObjectName("examinationDateLabel")
        self.commentsLabel = QtWidgets.QLabel(self.centralwidget)
        self.commentsLabel.setGeometry(QtCore.QRect(480, 450, 61, 16))
        self.commentsLabel.setObjectName("commentsLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 916, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.chooseImageButton.clicked.connect(self.setImage)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "START"))
        self.chooseImageButton.setText(_translate("MainWindow", "Przeglądaj.."))
        self.inputImageLabel.setText(_translate("MainWindow", "Obraz wejściowy"))
        self.sinogramLabel.setText(_translate("MainWindow", "Sinogram"))
        self.outputImageLabel.setText(_translate("MainWindow", "Obraz wynikowy"))
        self.chooseImageLabel.setText(_translate("MainWindow", "Wybierz obraz"))
        self.alphaStepLabel.setText(_translate("MainWindow", "Krok delta-alfa"))
        self.numOfDetectorsLabel.setText(_translate("MainWindow", "Liczba detektorów"))
        self.angularRangeLabel.setText(_translate("MainWindow", "Rozpiętość kątowa"))
        self.progressLabel.setText(_translate("MainWindow", "Postęp"))
        self.filterCheckbox.setText(_translate("MainWindow", "Filtrowanie"))
        self.patientNameLabel.setText(_translate("MainWindow", "Nazwisko"))
        self.examinationDateLabel.setText(_translate("MainWindow", "Data badania"))
        self.commentsLabel.setText(_translate("MainWindow", "Komentarze"))


    def setImage(self):
        self.imagePath, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Wybierz obraz", "",
                                                                  "Image Files (*.png *.jpg *.jpeg *.bmp);; Dicom Files (*.dcm)")
        if self.imagePath:
            if not self.imagePath.endswith(".dcm"):
                pixmap = QtGui.QPixmap(self.imagePath)
                pixmap = pixmap.scaled(self.inputImage.width(), self.inputImage.height(), QtCore.Qt.KeepAspectRatio)
                self.inputImage.setPixmap(pixmap)
                self.inputImage.setAlignment(QtCore.Qt.AlignCenter)
            else:
                ds = pydicom.dcmread(self.imagePath)
                print(ds.file_meta.MediaStorageSOPClassUID, ds.file_meta.MediaStorageSOPInstanceUID,
                      ds.file_meta.ImplementationClassUID)
                patientName = ds.PatientName
                patientID = ds.PatientID
                patientSex = ds.PatientSex
                # studyDate = ds.data_element("StudyDate")
                print(patientName, patientID, patientSex)
                if patientName:
                    self.patientNameTextfield.setText(str(patientName))
                # TODO READ THE REST OF DATA PRESENT IN UPLOADED DICOM
                # UWAGA!!! Wykrzacza się jeśli dane danego typu nie były podane. Testować na razie dla własnego wygenerowanego pliku dicom

                image = ds.pixel_array
                image = np.multiply(image, 255.0 / np.max(image))
                image = image.astype('uint8')
                io.imsave("dicom.png", image)
                pixmap = QtGui.QPixmap("dicom.png")
                pixmap = pixmap.scaled(self.inputImage.width(), self.inputImage.height(), QtCore.Qt.KeepAspectRatio)
                self.inputImage.setPixmap(pixmap)
                self.inputImage.setAlignment(QtCore.Qt.AlignCenter)

    def showSinogram(self, width):
        img = QtGui.QImage(self.sinogramPath)
        img2 = img.copy(0, 0, width, img.height())
        pixmap = QtGui.QPixmap(img2)
        pixmap = pixmap.scaled(self.sinogram.width(), self.sinogram.height(), QtCore.Qt.KeepAspectRatio)
        self.sinogram.setPixmap(pixmap)
        self.sinogram.setAlignment(QtCore.Qt.AlignLeft)

    def showReconstructed(self):
        img = QtGui.QImage(self.reconstructedPath)
        pixmap = QtGui.QPixmap(img)
        pixmap = pixmap.scaled(self.outputImage.width(), self.outputImage.height(), QtCore.Qt.KeepAspectRatio)
        self.outputImage.setPixmap(pixmap)
        self.outputImage.setAlignment(QtCore.Qt.AlignLeft)


    def startProcessing(self):
        self.generateSinogram(float(self.alphaStepTextfield.text()), int(self.numOfDetectorsTextfield.text()),
                              int(self.angularRangeTextfield.text()))

    def generateSinogram(self, step, numOfDetectors, angleRange):
        img = io.imread(self.imagePath)
        img = color.rgb2gray(img)
        if max(len(img), len(img[0])) > 1000:
            factor = 0.125
        else:
            factor = 0.25
        img = rescale(img, factor, anti_aliasing=False)
        m = len(img[0]) // 2
        n = len(img) // 2
        sinogram = np.zeros((numOfDetectors, int(180 / step)))
        radius = ((len(img) ** 2 + len(img[0]) ** 2) ** 0.5) / 2
        for k in np.arange(1, 180.5, step):
            angles = np.linspace(k, k + angleRange, numOfDetectors)
            detectorAngles = np.copy(angles)
            detectorAngles = np.flip(detectorAngles)
            detectorAngles += 180
            if numOfDetectors % 2 == 0:
                a = sin(radians((angles[numOfDetectors // 2 - 1] + angles[numOfDetectors // 2]) / 2)) / cos(radians((angles[numOfDetectors // 2 - 1] + angles[numOfDetectors // 2]) / 2))
            else:
                a = sin(radians(angles[numOfDetectors // 2])) / cos(radians(angles[numOfDetectors // 2]))
            #print(k, a)
            for i, angle in enumerate(angles):
                emiterX = int(round(radius * cos(radians(angle))))
                emiterY = int(round(radius * sin(radians(angle))))
                detectorX = int(round(radius * cos(radians(detectorAngles[i]))))
                detectorY = int(round(radius * sin(radians(detectorAngles[i]))))
                b = emiterY - a * emiterX
                deltax = detectorX - emiterX
                deltay = detectorY - emiterY
                error = 0
                if a <= -1:
                    if deltay == 0:
                        deltay = 0.000001
                    deltaerr = abs(deltax / deltay)
                    x = emiterX
                    for y in range(emiterY, detectorY + 1, -1):
                        if len(img) > y + n >= 0 and len(img[0]) > x + m >= 0:
                            sinogram[i][int((180 - k) / step)] += img[y + n][x + m]
                        error += deltaerr
                        if error >= 0.5:
                            x = x + 1
                            error -= 1
                elif -1 < a < 0:
                    if deltax == 0:
                        deltax = 0.000001
                    deltaerr = abs(deltay / deltax)
                    y = emiterY
                    for x in range(emiterX, detectorX + 1):
                        if len(img) > y + n >= 0 and len(img[0]) > x + m >= 0:
                            sinogram[i][int((180 - k) / step)] += img[y + n][x + m]
                        error += deltaerr
                        if error >= 0.5:
                            y = y - 1
                            error -= 1
                elif 0 < a < 1:
                    if deltax == 0:
                        deltax = 0.000001
                    deltaerr = abs(deltay / deltax)
                    error = 0
                    y = detectorY
                    for x in range(detectorX, emiterX + 1, -1):
                        if len(img) > y + n >= 0 and len(img[0]) > x + m >= 0:
                            sinogram[i][int((180 - k) / step)] += img[y + n][x + m]
                        error += deltaerr
                        if error >= 0.5:
                            y = y - 1
                            error -= 1
                elif a >= 1:
                    if deltay == 0:
                        deltay = 0.000001
                    deltaerr = abs(deltax / deltay)
                    x = detectorX
                    for y in range(detectorY, emiterY + 1, -1):
                        if len(img) > y + n >= 0 and len(img[0]) > x + m >= 0:
                            sinogram[i][int((180 - k) / step)] += img[y + n][x + m]
                        error += deltaerr
                        if error >= 0.5:
                            x = x - 1
                            error -= 1
        io.imsave("sinogram.png", resize(sinogram, (191, 251)))
        self.sinogramPath = "sinogram.png"
        self.progressSlider.setMinimum(0)
        self.progressSlider.setMaximum(251)
        self.progressSlider.setSingleStep(1)
        self.progressSlider.valueChanged.connect(self.showSinogram)



        reconstructedImage = np.zeros((len(img), len(img[0])))
        for k in np.arange(1, 181, step):
            angles = np.linspace(k, k + angleRange, numOfDetectors)
            detectorAngles = np.copy(angles)
            detectorAngles = np.flip(detectorAngles)
            detectorAngles += 180
            if numOfDetectors % 2 == 0:
                a = sin(radians((angles[numOfDetectors // 2 - 1] + angles[numOfDetectors // 2]) / 2)) / cos(
                    radians((angles[numOfDetectors // 2 - 1] + angles[numOfDetectors // 2]) / 2))
            else:
                a = sin(radians(angles[numOfDetectors // 2])) / cos(radians(angles[numOfDetectors // 2]))
            #print(k, a)
            for i, angle in enumerate(angles):
                emiterX = int(round(radius * cos(radians(angle))))
                emiterY = int(round(radius * sin(radians(angle))))
                detectorX = int(round(radius * cos(radians(detectorAngles[i]))))
                detectorY = int(round(radius * sin(radians(detectorAngles[i]))))
                b = emiterY - a * emiterX
                deltax = detectorX - emiterX
                deltay = detectorY - emiterY
                error = 0
                if a <= -1:
                    if deltay == 0:
                        deltay = 0.000001
                    deltaerr = abs(deltax / deltay)
                    x = emiterX
                    for y in range(emiterY, detectorY + 1, -1):
                        if len(img) > y + n >= 0 and len(img[0]) > x + m >= 0:
                            reconstructedImage[y + n][x + m] += sinogram[i][int((180 - k) / step - 1)]
                        error += deltaerr
                        if error >= 0.5:
                            x = x + 1
                            error -= 1
                elif -1 < a < 0:
                    if deltax == 0:
                        deltax = 0.000001
                    deltaerr = abs(deltay / deltax)
                    y = emiterY
                    for x in range(emiterX, detectorX + 1):
                        if len(img) > y + n >= 0 and len(img[0]) > x + m >= 0:
                            reconstructedImage[y + n][x + m] += sinogram[i][int((180 - k) / step - 1)]
                        error += deltaerr
                        if error >= 0.5:
                            y = y - 1
                            error -= 1
                elif 0 < a < 1:
                    if deltax == 0:
                        deltax = 0.000001
                    deltaerr = abs(deltay / deltax)
                    error = 0
                    y = detectorY
                    for x in range(detectorX, emiterX + 1, -1):
                        if len(img) > y + n >= 0 and len(img[0]) > x + m >= 0:
                            reconstructedImage[y + n][x + m] += sinogram[i][int((180 - k) / step - 1)]
                        error += deltaerr
                        if error >= 0.5:
                            y = y - 1
                            error -= 1
                elif a >= 1:
                    if deltay == 0:
                        deltay = 0.000001
                    deltaerr = abs(deltax / deltay)
                    x = detectorX
                    for y in range(detectorY, emiterY + 1, -1):
                        if len(img) > y + n >= 0 and len(img[0]) > x + m >= 0:
                            reconstructedImage[y + n][x + m] += sinogram[i][int((180 - k) / step - 1)]
                        error += deltaerr
                        if error >= 0.5:
                            x = x - 1
                            error -= 1

        suma = np.sum(sinogram) / len(sinogram[0])
        for i in range(len(reconstructedImage)):
            for j in range(len(reconstructedImage[i])):
                reconstructedImage[i][j] -= suma
                if reconstructedImage[i][j] < 0:
                    reconstructedImage[i][j] = 0

        '''
        UWAGA 
        dopisałam tutaj konwersję obrazu (zrekonstruowanego), żeby nie było erroru o stratnym zapisie
        Według mnie nic ona nie zmienia ale wolę żeby była
        Jakbys jednak zauważył jakieś problemy pozbądz sie jej bez wahania
        '''
        reconstructedImage = np.multiply(reconstructedImage, 255.0 / np.max(reconstructedImage))
        reconstructedImage = reconstructedImage.astype('uint8')

        file_meta = Dataset()
        file_meta.MediaStorageSOPClassUID = "1.2.840.10018.5.1.4.1.1.7"
        file_meta.MediaStorageSOPInstanceUID = "1.2.276.0.7240010.3.1.4.3846053626.3968.1286299971.696"
        file_meta.ImplementationClassUID = "1.2.276.0.7240010.3.0.3.5.5"

        print("Setting dataset values...")
        # Create the FileDataset instance (initially no data elements, but file_meta
        # supplied)
        ds = FileDataset("plik.dcm", {},
                         file_meta=file_meta, preamble=b"\0" * 128)

        # TODO Pobrać z GUI resztę danych o pacjencie, które chcemy zapisywać/odczytywać
        ds.PatientName = self.patientNameTextfield.toPlainText()
        ds.PatientID = "123456"
        ds.StudyDate = self.dateEdit.dateTime().toString()
        ds.StudyID = "987987987"
        ds.PatientSex = "M"

        # DANE O OBRAZIE, NA RAZIE NIE ZMIENIAC!!!
        ds.PixelData = reconstructedImage.tobytes()
        ds.BitsAllocated = 8
        ds.Rows = len(reconstructedImage)
        ds.Columns = len(reconstructedImage[0])
        ds.PixelRepresentation = 0
        ds.SamplesPerPixel = 1
        ds.BitsStored = 16 #8
        ds.HighBit = 15 #7
        ds.PhotometricInterpretation = "MONOCHROME2"

        # ds.StudyInstanceUID = "1.2.276.0.7230010.3.1.2.3846053626.3968.1286299971.694"
        # Set the transfer syntax
        ds.is_little_endian = True
        ds.is_implicit_VR = True
        # Set creation date/time
        dt = datetime.datetime.now()
        ds.ContentDate = dt.strftime('%Y%m%d')
        timeStr = dt.strftime('%H%M%S.%f')  # long format with micro seconds
        ds.ContentTime = timeStr
        ds.save_as("plik.dcm")
        ds.file_meta.TransferSyntaxUID = pydicom.uid.ExplicitVRBigEndian
        ds.is_little_endian = False
        ds.is_implicit_VR = False

        print("Writing test file as Big Endian Explicit VR", "plik.dcm")
        ds.save_as("plik.dcm")

        self.reconstructedPath = "reconstructed.png"
        io.imsave(self.reconstructedPath, reconstructedImage)
        self.showReconstructed()




def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    sys.excepthook = except_hook
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

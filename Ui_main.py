# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Administrator\eric6\test01\main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import random

from PyQt5 import QtCore, QtGui, QtWidgets
import win32clipboard as wc
import os

from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(231, 108)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralWidget)
        self.pushButton.clicked.connect(self.getCopy)
        MainWindow.setWindowFlag(Qt.WindowStaysOnTopHint)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ramdom"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton.setShortcut(_translate("MainWindow", "Ctrl+X"))

    def getCopy(self):
        result = ''
        # read file
        with open('area.txt', 'r', encoding='utf-8') as file:
            result = file.readlines()
        result = [x.strip() for x in result]
        length = len(result) - 1
        position = random.randint(0, length)
        text = result[position]
        self.copyText(text)
        print(text)

    def copyText(self, text):
        wc.OpenClipboard()
        wc.EmptyClipboard()
        wc.SetClipboardText(text)
        wc.CloseClipboard()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

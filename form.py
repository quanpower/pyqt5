# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(320, 240)
        Form.setStyleSheet("border-color: rgb(239, 41, 41);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 160, 151, 51))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 20, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 57 20pt \"Ubuntu\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 81, 17))
        self.label_2.setStyleSheet("color: rgb(204, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 71, 17))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(150, 70, 151, 17))
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(150, 110, 141, 17))
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "开始/结束"))
        self.label.setText(_translate("Form", "NO"))
        self.label_2.setText(_translate("Form", "start_time"))
        self.label_3.setText(_translate("Form", "end_time"))
        self.label_4.setText(_translate("Form", "start_time_str"))
        self.label_5.setText(_translate("Form", "end_time_str"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QMenu, QApplication, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from form import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        # exitAct = QAction(QIcon('exit.png'), '&Exit', self)        
        # exitAct.setShortcut('Ctrl+Q')
        # exitAct.setStatusTip('Exit application')
        # exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        # menubar = self.menuBar()
        # fileMenu = menubar.addMenu('&File')
        # fileMenu.addAction(exitAct)

        MainWindow.setStatusBar(self.statusbar)
        self.statusBar().showMessage('Ready')

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.grid = QGridLayout()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setStyleSheet("#MainWindow{background-color: blue}")


    def contextMenuEvent(self, event):
   
       cmenu = QMenu(self)
       
       newAct = cmenu.addAction("New")
       opnAct = cmenu.addAction("Open")
       quitAct = cmenu.addAction("Quit")
       action = cmenu.exec_(self.mapToGlobal(event.pos()))
       
       if action == quitAct:
           qApp.quit()

    def keyPressEvent(self, e):
        
        if e.key() == Qt.Key_Escape:
            self.close()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
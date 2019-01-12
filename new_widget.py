import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class spindemo(QWidget):
    def __init__(self, parent=None):
        super(spindemo, self).__init__(parent)
        self.setWindowTitle("SpinBox 例子")
        self.resize(300, 100)

        # self.verticalLayoutWidget = QWidget()
        # self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 301, 221))
        # self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
      
  
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel("label")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.label_3 = QtWidgets.QLabel("label_3")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_2 = QtWidgets.QLabel("label_2")
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout_2)

        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel("label_5")
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel("label_4")
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.pushButton = QtWidgets.QPushButton("pushButton")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)

        # self.verticalLayout = QVBoxLayout()
        # self.l1=QLabel("current value:")
        # self.l1.setAlignment(Qt.AlignCenter)
        # self.verticalLayout.addWidget(self.l1)


        # self.sp = QSpinBox()
        # layout.addWidget(self.sp)
        # self.sp2 = QSpinBox()
        # layout.addWidget(self.sp2)


        # self.sp.valueChanged.connect(self.valuechange)
        self.setLayout(self.verticalLayout)
              
    def valuechange(self):  
        self.l1.setText("current value:" + str(self.sp.value()) )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = spindemo()
    ex.show()
    sys.exit(app.exec_())
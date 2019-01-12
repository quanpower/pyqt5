import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from new_widget import *
from main5 import *
class MyWindow(Example4):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__()
        # self.setupUi(self)

        self.s1=spindemo()
        self.s1.show()
        self.layout.addWidget(self.s1,1,1)

        self.s2=spindemo()
        self.s2.show()
        self.layout.addWidget(self.s2,1,2)

        self.s3=spindemo()
        self.s3.show()
        self.layout.addWidget(self.s3,1,3)

        self.s4=spindemo()
        self.s4.show()
        self.layout.addWidget(self.s4,2,1)

        self.s5=spindemo()
        self.s5.show()
        self.layout.addWidget(self.s5,2,2)

        self.s6=spindemo()
        self.s6.show()
        self.layout.addWidget(self.s6,2,3)

        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
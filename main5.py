#coding=utf-8
import sys
from PyQt5.QtWidgets import QMainWindow, QWidget,QGridLayout, QPushButton,QApplication, QMenuBar, QAction, qApp, QTextEdit, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class Example4(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.resize(800, 600)
        self.layout = QGridLayout()

        self.centralwidget = QWidget()
        self.centralwidget.setLayout(self.layout)

        self.setCentralWidget(self.centralwidget)
        # self.setCentralWidget(textEdit)

        # # 创建一个Action
        # exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        # exitAction.setShortcut('Ctrl+Q')
        # exitAction.setStatusTip('退出程序')
        # exitAction.triggered.connect(self.close)

        # # 底部状态栏
        # self.statusBar().showMessage('状态栏看我')

        # # 顶部菜单栏
        # menubar = self.menuBar()
        # menubar.setNativeMenuBar(False)
        # fileMenu = menubar.addMenu('File')
        # fileMenu.addAction(exitAction)

        # # 次顶部的工具栏
        # toolbar = self.addToolBar('Exit')
        # toolbar.addAction(exitAction)

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('QMainWindow综合使用')
        self.show()

def main4():
    app = QApplication(sys.argv)
    example = Example4()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main4()

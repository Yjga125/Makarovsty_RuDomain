import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication
from PySide2 import QtWidgets
from Chat import Ui_Chat
import SMTP

#class clientchat(QtWidgets.QMainWindow, Ui_Chat):
    #def __init__(self):
        #super().__init__()
        # Создание формы и Ui (наш дизайн)
        #self.setupUi(self)
        # Показать наше окно
        #self.show()
        #self.send.clicked.connect(SMTP.Ru_To_Google)
        
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        # '''QToolTip.setFont(QFont('SansSerif', 10))

        # self.setToolTip('This is a <b>QWidget</b> widget')

        # btn = QPushButton('Button', self)
        # btn.setToolTip('This is a <b>QPushButton</b> widget')
        # btn.resize(btn.sizeHint())
        # btn.move(150, 50)'''

        qbtn = QPushButton('Google_To_En', self)
        qbtn.clicked.connect(SMTP.Google_To_En)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        qbtn = QPushButton('En_To_En', self)
        qbtn.clicked.connect(SMTP.En_To_En)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(200, 50)

        qbtn = QPushButton('Google_To_Google', self)
        qbtn.clicked.connect(SMTP.Google_To_Google)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 100)

        qbtn = QPushButton('En_To_Ru', self)
        qbtn.clicked.connect(SMTP.En_To_Ru)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(200, 100)

        qbtn = QPushButton('Ru_To_En', self)
        qbtn.clicked.connect(SMTP.Ru_To_En)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(200, 150)

        qbtn = QPushButton('Ru_To_Ru', self)
        qbtn.clicked.connect(SMTP.Ru_To_Ru)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 150)
        
        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

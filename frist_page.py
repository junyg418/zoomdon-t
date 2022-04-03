from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import sys
import a_1

class Gui(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(500, 700)
        # self.setGeometry(100, 100, 1024, 768)
        self.setWindowTitle('easy한 학교 생활')
        # self.setMaximumSize(500,750)
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.Info()

    def Info(self):
        self.Mainlay = QGridLayout()
        self.Mainlay.setRowStretch(0,2)
        self.Mainlay.setRowStretch(1,3)
        self.Mainlay.setRowStretch(2,7)
        self.setLayout(self.Mainlay)

        self.funny_school = QLabel('Easy 한 학교생활',self)
        self.funny_school.setAlignment(QtCore.Qt.AlignCenter)
        self.funny_school.setFont(QtGui.QFont('궁서',20))
        self.Mainlay.addWidget(self.funny_school)

        self.Stu_btn = QPushButton()
        self.Stu_btn.clicked.connect(self.to_go_a_1)
        self.Stu_btn.setMinimumSize(270,245)
        self.Stu_btn.setMaximumSize(270,245)
        # self.Stu_btn.resize(200,200)
        self.Stu_btn.setStyleSheet('background-image:url(./학생.PNG)')
        self.Mainlay.addWidget(self.Stu_btn, 1, 0)

        # self.Mainlay.addItem(, 2, 0)

    def to_go_a_1(self):
        self.a_1info = a_1.LinkAccepting()
        self.a_1info.show()
        self.close()
        


app = QApplication(sys.argv)
ex = Gui()
ex.show()
sys.exit(app.exec_()) 


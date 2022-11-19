import sys
from random import randint

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(93, 28))
        self.pushButton.setMaximumSize(QtCore.QSize(93, 28))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Git "))
        self.pushButton.setText(_translate("MainWindow", "Создать"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        uic.loadUi('git2.ui', self)  # Загружаем дизайн
        self.do_paint = False
        self.pos = None

        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.pos = True

        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    # def paint(self):
    #     self.do_paint = True
    #     self.repaint()

    def draw(self, qp):
        if self.pos:
            # self.pushButton.close()
            for i in range(15):
                z = randint(10, 100)
                # self.cord = (int(self.cord[0] - z / 2), int(self.cord[1] - z / 2))
                qp.setBrush(QColor(255, 255, 0))
                qp.drawEllipse(randint(10, 500), randint(10, 500), z, z)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

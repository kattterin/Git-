import sys
from random import randint

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from git2 import Ui_MainWindow


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


    def draw(self, qp):
        if self.pos:
            # self.pushButton.close()
            for i in range(10):
                z = randint(10, 100)
                # self.cord = (int(self.cord[0] - z / 2), int(self.cord[1] - z / 2))
                qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
                qp.drawEllipse(randint(10, 500), randint(10, 500), z, z)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

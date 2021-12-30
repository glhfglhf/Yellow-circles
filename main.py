import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.draw = False
        self.setMouseTracking(True)
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        if not self.draw:
            return
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.draw_someth(qp)
        # Завершаем рисование
        qp.end()

    def draw_someth(self, qp):
        # Задаем кисть
        qp.setBrush(QColor(255, 255, 0))
        # Рисуем прямоугольник заданной кистью
        size = randint(20, 250)
        qp.drawEllipse(self.x - size // 2, self.y - size // 2, size, size)

    def run(self):
        self.x, self.y = 380, 275
        self.draw = True
        self.repaint()
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.draw_someth(qp)
        # Завершаем рисование
        qp.end()
        self.draw = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

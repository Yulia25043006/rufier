from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QApplication
from ThirdWindow import *

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connect()
        self.set_appear()
        self.show()
    def initUI(self):
        self.label1 = QLabel('Лягте на спину и замерьте пульс на 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить '
                             'таймер.Результат запишите в соответствующее полe')
        self.label2 = QLabel('Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания", чтобы запустить счетчик приседаний')
        self.button = QPushButton('Начать первый тест')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
    def next(self):
        self.third_window = ThirdWindow()
        self.hide()
    def connect(self):
        self.button.clicked.connect(next)
    def set_appear(self):
         self.setWindowTitle('Начать делать приседания')
         self.resize(500, 500)
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QApplication
class ThirdWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connect()
        self.set_appear()
        self.show()
    def initUI(self):
        self.label1 = QLabel('Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.'
                             'Нажмите кнопку "Начать финальный тест", чтобы запустить таймер.'
                             'Зеленым обозначены секунды, в течение которых необходимо проводить измерения, черным- '
                             'секунды без замера пульсаций. Размеры запишите в соответствующие поля.')
        self.button = QPushButton('Начать финальный тест')
        self.layout = QVBoxLayout
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
    def connect(self):
        self.button.clicked.connect(next)
    def set_appear(self):
        self.setWindowTitle('запустить таймер')
        self.resize(500, 500)

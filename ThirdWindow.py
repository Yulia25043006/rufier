from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QApplication
class ThirdWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_appear()
        self.show()
    def initUI(self):
        self.label1 = QLabel('Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\nНажмите кнопку "Начать финальный тест", чтобы запустить таймер.\nЗелёным обозначены секунды, в течение которых необходимо \nпроводить измерения, черным - секунды без замера пульсаций. Результаты запишите в соответствующие поля.')

        self.button = QPushButton('Начать финальный тест')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
    def set_appear(self):
        self.setWindowTitle('запустить таймер')
        self.resize(500, 500)

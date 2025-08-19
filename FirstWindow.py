from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QApplication
from SecondWindow import *

class FirstWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connect()
        self.set_appear()
        self.show()
    def initUI(self):
        self.label1 = QLabel('Добро пожаловать в программу по определению состояния здоровья!')
        self.label2 = QLabel('Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.\n'
                   'Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\n'
                   'У испытуемого, находящегося в положении лежа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;\n'
                   'затем в течение 45 секунд испытуемый выполняет 30 приседаний.\n'
                   'После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,\n'
                   'а потом — за последние 15 секунд первой минуты периода восстановления.\n'
                   'Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в\n'
                   'ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.')
        self.button = QPushButton('начать')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)
    def next(self):
        self.second_window = SecondWindow()
        self.hide()
    def connect(self):
        self.button.clicked.connect(next)
    def set_appear(self):
        self.setWindowTitle('здоровье')
        self.resize(500, 500)
app = QApplication([])
first_window = FirstWindow()
app.exec()


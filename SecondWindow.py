from PyQt6.QtCore import QTime, QTimer
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QApplication, QLineEdit, QHBoxLayout
from ThirdWindow import ThirdWindow

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connect()
        self.set_appear()
        self.show()
    def initUI(self):
        self.label1 = QLabel('Введите ФИО')
        self.label2 = QLabel('возраст')
        self.label3 = QLabel('Лягте на спину и замерьте пульс на 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить '
                             'таймер.Результат запишите в соответствующее полe')
        self.label4 = QLabel('Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания", чтобы запустить счетчик приседаний')
        self.label5 = QLabel('Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\nНажмите кнопку "Начать финальный тест", чтобы запустить таймер.\nЗелёным обозначены секунды, в течение которых необходимо \nпроводить измерения, черным - секунды без замера пульсаций. Результаты запишите в соответствующие поля.')
        self.edit1 = QLineEdit('ФИО')
        self.edit2 = QLineEdit('0')
        self.edit3 = QLineEdit('0')
        self.edit4 = QLineEdit('0')
        self.edit5 = QLineEdit('0')
        self.button1 = QPushButton('Начать первый тест')
        self.button2 = QPushButton('Начать второй тест')
        self.button3 = QPushButton('Начать делать третий тест')
        self.button4 = QPushButton('Отправить результаты')
        self.timer_text = QLabel('00:00:00')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.edit1)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.edit2)
        self.layout.addWidget(self.label3)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.edit3)
        self.layout.addWidget(self.label4)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.label5)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.edit4)
        self.layout.addWidget(self.edit5)
        self.layout.addWidget(self.button4)
        self.layoutk = QHBoxLayout()
        self.layoutk.addLayout(self.layout)
        self.layoutk.addWidget(self.timer_text)
        self.setLayout(self.layoutk)

    def timer1(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timerEvent1)
        self.timer.start(1000)

    def timerEvent1(self):
        global time
        time = time.addSecs(-1)
        self.timer_text.setText(time.toString('hh:mm:ss'))
        self.timer_text.setStyleSheet('color: rgb(0, 0, 230)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
    def next(self):
        self.exp = Experiment(self.edit1.text(), self.edit2.text(), self.edit3.text(), self.edit4.text())
        self.third_window = ThirdWindow(self.exp)
        self.hide()

    def timer2(self):
        global time
        time = QTime(0, 0, 45)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timerEvent1)
        self.timer.start(1000)

    def timerEvent2(self):
        global time
        time = time.addSecs(-1)
        self.timer_text.setText(time.toString('hh:mm:ss'))
        self.timer_text.setStyleSheet('color: rgb(255, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()
    def connect(self):
        self.button2.clicked.connect(self.timer2)
        self.button4.clicked.connect(self.next)
        self.button1.clicked.connect(self.timer1)
        self.button3.clicked.connect(self.timer3)
    def set_appear(self):
         self.setWindowTitle('Начать делать приседания')
         self.resize(500, 500)

    def timer3(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timerEvent1)
        self.timer.start(1000)

    def timerEvent3(self):
        global time
        time = time.addSecs(-1)
        self.timer_text.setText(time.toString('hh:mm:ss'))
        self.timer_text.setStyleSheet('color: rgb(80, 200, 120)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

class Experiment():
    def __init__(self, edit1, edit2, edit3, edit4):
        self.age = edit1
        self.t1 = edit2
        self.t2 = edit3
        self.t3 = edit4

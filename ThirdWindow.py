from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QApplication
txt_res1 = "низкая. Срочно обратитесь к врачу!"
txt_res2 = "удовлетворительная. Обратитесь к врачу!"
txt_res3 = "средняя. Возможно, стоит дополнительно обследоваться у врача."
txt_res4 = "выше среднего"
txt_res5 = "высокая"
class ThirdWindow(QWidget):
    def __init__(self, experiment):
        super().__init__()
        self.exp = experiment
        self.initUI()
        self.set_appear()
        self.res = self.result()
        self.show()
    def initUI(self):
        self.label1 = QLabel('Индекс Руфье:' + str(self.index))
        self.label2 = QLabel(self.res)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.label2)
        self.setLayout(self.layout)
    def set_appear(self):
        self.setWindowTitle('запустить таймер')
        self.resize(500, 500)
    def result(self):
        if self.exp.age < 7:
            self.index = 0
            return "нет данных для такого возраста"
        self.index = (4 * (int(self.exp.t1) + int(self.exp.t2) + int(self.exp.t3)) - 200) / 10
        if self.exp.age == 7 or self.exp.age == 8:
            if self.index >= 21:
                return txt_res1
            elif self.index < 21 and self.index >= 17:
                return txt_res2
            elif self.index < 17 and self.index >= 12:
                return txt_res3
            elif self.index < 12 and self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 9 or self.exp.age == 10:
            if self.index >= 19.5:
                return txt_res1
            elif self.index < 19.5 and self.index >= 15.5:
                return txt_res2
            elif self.index < 15.5 and self.index >= 10.5:
                return txt_res3
            elif self.index < 10.5 and self.index >= 5:
                return txt_res4
            else:
                return txt_res5

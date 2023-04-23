from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QLineEdit, QGridLayout, QSizePolicy
)
from PyQt5.QtGui import QFont


my_font = QFont('Segoe UI', 18)


class StretchButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(40, 40)
        self.setFont(my_font)

        

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Калькулятор')

        self.to_solve = ''

        self.display = QLineEdit()
        self.display.setReadOnly(True)

        btn_0 = StretchButton('0')
        btn_1 = StretchButton('1')
        btn_2 = StretchButton('2')
        btn_3 = StretchButton('3')
        btn_4 = StretchButton('4')
        btn_5 = StretchButton('5')
        btn_6 = StretchButton('6')
        btn_7 = StretchButton('7')
        btn_8 = StretchButton('8')
        btn_9 = StretchButton('9')
        btn_back = StretchButton('<-')
        btn_clear = StretchButton('C')
        btn_add = StretchButton('+')
        btn_substract = StretchButton('-')
        btn_multiply = StretchButton('*')
        btn_divide = StretchButton('/')
        btn_result = StretchButton('=')
        btn_point = StretchButton('.')

        
        layout = QGridLayout()
        layout.addWidget(self.display, 0, 0, 1, 4)
        layout = QGridLayout()
        layout.addWidget(self.display, 0, 0, 1, 4)

        layout.addWidget(btn_back, 1, 0)
        layout.addWidget(btn_clear, 1, 1)
        layout.addWidget(btn_add, 1, 2)
        layout.addWidget(btn_substract, 1, 3)

        layout.addWidget(btn_7, 2, 0)
        layout.addWidget(btn_8, 2, 1)
        layout.addWidget(btn_9, 2, 2)
        layout.addWidget(btn_multiply, 2, 3)

        layout.addWidget(btn_4, 3, 0)
        layout.addWidget(btn_5, 3, 1)
        layout.addWidget(btn_6, 3, 2)
        layout.addWidget(btn_divide, 3, 3)

        layout.addWidget(btn_1, 4, 0)
        layout.addWidget(btn_2, 4, 1)
        layout.addWidget(btn_3, 4, 2)
        layout.addWidget(btn_result, 4, 3, 2, 1)

        layout.addWidget(btn_0, 5, 0, 1, 2)
        layout.addWidget(btn_point, 5, 2)

        self.setLayout(layout)

        btn_0.clicked.connect(self.btn_handler)
        btn_1.clicked.connect(self.btn_handler)
        btn_2.clicked.connect(self.btn_handler)
        btn_3.clicked.connect(self.btn_handler)
        btn_4.clicked.connect(self.btn_handler)
        btn_5.clicked.connect(self.btn_handler)
        btn_6.clicked.connect(self.btn_handler)
        btn_7.clicked.connect(self.btn_handler)
        btn_8.clicked.connect(self.btn_handler)
        btn_9.clicked.connect(self.btn_handler)
        btn_divide.clicked.connect(self.btn_handler)
        btn_multiply.clicked.connect(self.btn_handler)
        btn_result.clicked.connect(self.btn_handler)
        btn_add.clicked.connect(self.btn_handler)
        btn_substract.clicked.connect(self.btn_handler)
        btn_point.clicked.connect(self.btn_handler)
        btn_back.clicked.connect(self.btn_handler)
        btn_clear.clicked.connect(self.btn_handler)


    def btn_handler(self):
        btn = self.sender()
        if btn.text() in '0123456789/*-+.':
            self.to_solve += btn.text()
        elif btn.text == '<-':
            self.to_solve = self.to_solve[0:-1]
        elif btn.text() == 'C':
            self.to_solve = ''
        elif btn.text() == '=':
            try:
                self.to_solve = str(eval(self.to_solve))
            except:
                self.to_solve = '0'
        self.display.setText(self.to_solve)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()

from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QLineEdit, QGridLayout
)
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Калькулятор')

        self.display = QLineEdit()
        self.display.setReadOnly(True)

        btn_0 = QPushButton('0')
        btn_1 = QPushButton('1')
        btn_2 = QPushButton('2')
        btn_3 = QPushButton('3')
        btn_4 = QPushButton('4')
        btn_5 = QPushButton('5')
        btn_6 = QPushButton('6')
        btn_7 = QPushButton('7')
        btn_8 = QPushButton('8')
        btn_9 = QPushButton('9')
        btn_back = QPushButton('<-')
        btn_clear = QPushButton('C')
        btn_add = QPushButton('+')
        btn_substract = QPushButton('-')
        btn_multiply = QPushButton('*')
        btn_divide = QPushButton('/')
        btn_result = QPushButton('=')
        btn_point = QPushButton('.')
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        
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




app = QApplication([])
window = MainWindow()
window.show()
app.exec()

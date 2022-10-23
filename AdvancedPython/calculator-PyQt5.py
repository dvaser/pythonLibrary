from decimal import DivisionByZero
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from PyQt5.QtGui import QIcon

class Qt():
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.win = Calculator()
        self.win.show()
        sys.exit(self.app.exec())

class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(200,200,332,180)
        self.setWindowIcon(QIcon("calculator.png"))
        self.initUI()

    def initUI(self):
        self.lbl_num1 = QtWidgets.QLabel(self)
        self.lbl_num1.setText("Num")
        self.lbl_num1.move(50,30)

        self.lbl_num2 = QtWidgets.QLabel(self)
        self.lbl_num2.setText("Num")
        self.lbl_num2.move(50,80)

        self.txt_num1 = QtWidgets.QLineEdit(self)
        self.txt_num1.resize(100,32)
        self.txt_num1.move(100,30)

        self.txt_num2 = QtWidgets.QLineEdit(self)
        self.txt_num2.resize(100,32)
        self.txt_num2.move(100,80)

        self.btn_add = QtWidgets.QPushButton(self)
        self.btn_add.setText("+")
        self.btn_add.resize(32,32)
        self.btn_add.move(210,35)
        self.btn_add.clicked.connect(self.calc)

        self.btn_extract = QtWidgets.QPushButton(self)
        self.btn_extract.setText("-")
        self.btn_extract.resize(32,32)
        self.btn_extract.move(250,35)
        self.btn_extract.clicked.connect(self.calc)

        self.btn_divide = QtWidgets.QPushButton(self)
        self.btn_divide.setText("/")
        self.btn_divide.resize(32,32)
        self.btn_divide.move(210,75)
        self.btn_divide.clicked.connect(self.calc)

        self.btn_multiply = QtWidgets.QPushButton(self)
        self.btn_multiply.setText("*")
        self.btn_multiply.resize(32,32)
        self.btn_multiply.move(250,75)
        self.btn_multiply.clicked.connect(self.calc)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText("Result")
        self.lbl_result.move(100,120)

    def calc(self):
        sender = self.sender()
        
        try:
            if(sender.text() == "+"):
                result = int(self.txt_num1.text()) + int(self.txt_num2.text())
            elif(sender.text() == "-"):
                result = int(self.txt_num1.text()) - int(self.txt_num2.text())
            elif(sender.text() == "/"):
                result = int(self.txt_num1.text()) / int(self.txt_num2.text())
            elif(sender.text() == "*"):
                result = int(self.txt_num1.text()) * int(self.txt_num2.text())
        except:
            result = 0

        self.lbl_result.setText("Result: " + str(result))

Qt()
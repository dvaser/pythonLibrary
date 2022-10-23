import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip, QWidget
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QPalette, QColor

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        # hlayout1 = QtWidgets.QHBoxLayout()    #? Create a Horizonal Layout
        # hlayout1.addWidget(Color("light pink"))
        # hlayout1.addWidget(Color("light blue"))
        # hlayout1.addWidget(Color("light green"))
        # hlayout1.setContentsMargins(30,20,0,30)   #? Margin (left, top, right, bottom)
        # hlayout1.setSpacing(30)   #? Space between widgets

        # hlayout2 = QtWidgets.QHBoxLayout()    #? Create a Horizonal Layout
        # hlayout2.addWidget(Color("purple"))
        # hlayout2.addWidget(Color("orange"))

        # vlayout = QtWidgets.QVBoxLayout()   #? Create a Vertical Layout
        # vlayout.addLayout(hlayout1)     #? Add h-ayout in v-layout
        # vlayout.addLayout(hlayout2)

        layout = QtWidgets.QGridLayout()
        layout.addWidget(Color("red"), 0,0)     #? (0,0) matrix in Grid Layout
        layout.addWidget(Color("light blue"), 1,1)     #? (1,1) matrix in Grid Layout
        layout.addWidget(Color("light green"), 0,2)     #? (0,2) matrix in Grid Layout

        widget = QWidget()
        widget.setLayout(layout)   #? Screen Layout Design
        self.setCentralWidget(widget)  #? Screen (window) color
        
        self.setWindowTitle("Application")   #? Window Title
        self.setGeometry(200,200,500,300)    #? (x, y, size-w, size-h)
        self.setWindowIcon(QIcon("icon.png"))    #? Icon
        self.setToolTip("Application")
        self.initUI()

    def initUI(self):
        self.lbl_name = QtWidgets.QLabel(self)     #? Label of win form
        self.lbl_name.setText("First Name: ")
        self.lbl_name.move(50,30)    #? (x, y)

        self.lbl_surname = QtWidgets.QLabel(self)     #? Label of win form
        self.lbl_surname.setText("Last Name: ")
        self.lbl_surname.move(50,70)    #? (x, y)

        self.lbl_result = QtWidgets.QLabel(self)     #? Label of win form
        self.lbl_result.move(150, 150)  #? (x, y)
        self.lbl_result.setText("Result")
        self.lbl_result.resize(300,50)

        self.txt_name = QtWidgets.QLineEdit(self)     #? Text of win form
        self.txt_name.move(150, 30)      #? (x, y)
        self.txt_name.resize(200,25)    #? (size-w, size-h)

        self.txt_surname = QtWidgets.QLineEdit(self)     #? Text of win form
        self.txt_surname.move(150, 70)      #? (x, y)
        self.txt_surname.resize(200,25)    #? (size-w, size-h)

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Save")
        self.btn_save.move(150,110)
        self.btn_save.clicked.connect(self.clicked)

    def clicked(self):
        self.lbl_result.setText(f"Name: {self.txt_name.text()}\nSurname: {self.txt_surname.text()}")

def window():
    app = QApplication(sys.argv)    #? be able to use System argument
    win = Window()             #? Create Window
    win.show()      #? Show Window
    sys.exit(app.exec())    #? use exec on app, for system exit

window()
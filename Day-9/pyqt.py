from cProfile import label
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        
        
def buttonclick():
    print("button click")

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(1280,720,300,300)
    win.setWindowTitle("Hosyn App")
    
    label = QtWidgets.QLabel(win)
    label.setText("First Label")
    label.move(50,50)
    
    b1 = QtWidgets.QPushButton(win)
    b1.setText("Click Me")
    b1.clicked.connect(buttonclick)
    
    win.show()
    sys.exit(app.exec_())

window()
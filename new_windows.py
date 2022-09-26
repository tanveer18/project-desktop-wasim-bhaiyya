import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainWindows(QWidget):
    def __init__(self):
        super(MainWindows, self).__init__()
        self.setWindowTitle("New Form")

        self.show()
app = QApplication([])
windows = MainWindows()
app.exec_()
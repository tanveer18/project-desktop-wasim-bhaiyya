import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# create a windows
app = QApplication(sys.argv)

# set the name of windows
windows = QWidget()

# set the label third for inputs
label1 = QLabel(windows)
label1.setText("Search : ")
label1.setFont(QFont("Arial",20))
label1.move(20,30)

# create inputs third text 1 for case type bar
label1_text = QLineEdit(windows)
label1_text.resize(300,50)
label1_text.setFont(QFont('Arial',20))
label1_text.move(260,20)

# create inputs third text2 for case number bar
label1_text = QLineEdit(windows)
label1_text.resize(300,50)
label1_text.setFont(QFont('Arial',20))
label1_text.move(600,20)


# set the label second inputs
label2 = QLabel(windows)
label2.setText("Record Room No : ")
label2.setFont(QFont("Arial",20))
label2.move(20,100)

# create inputs second for the record room no
label2_text = QLineEdit(windows)
label2_text.resize(300,50)
label2_text.setFont(QFont('Arial',20))
label2_text.move(260,90)

# create a button
btn = QPushButton(windows)
btn.setText("Update Record")
btn.setFont(QFont('Arial',15))
btn.resize(150,50)
btn.move(330,170)


# set the windows size
windows.setGeometry(1000,1000,1000,1000)

# set the windows Name
windows.setWindowTitle("Update Dashboard")

# windows show function
windows.show()

# set click exit to exit windows
sys.exit(app.exec_())
windows()
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# create a windows
app = QApplication(sys.argv)

# set the name of windows
windows = QWidget()

# set the first label for inputs
label1 = QLabel(windows)
label1.setText("Name of Client : ")
label1.setFont(QFont("Arial",20))
label1.move(20,30)

# create inputs first text bar
label1_text = QLineEdit(windows)
label1_text.resize(300,50)
label1_text.setFont(QFont('Arial',20))
label1_text.move(250,20)

# set the second label for input
label2 = QLabel(windows)
label2.setText("Versus : ")
label2.setFont(QFont("Arial Bold",20))
label2.move(560,30)

# create inputs second text bar
label2_text = QLineEdit(windows)
label2_text.resize(300,50)
label2_text.setFont(QFont('Arial',20))
label2_text.move(680,20)

# set the label third
label3 = QLabel(windows)
label3.setText("Case Number : ")
label3.setFont(QFont("Arial",20))
label3.move(20,110)

# create inputs third text 1 for case type bar
label3_text = QLineEdit(windows)
label3_text.resize(300,50)
label3_text.setFont(QFont('Arial',20))
label3_text.move(250,100)

# create inputs third text2 for case number bar
label3_text = QLineEdit(windows)
label3_text.resize(300,50)
label3_text.setFont(QFont('Arial',20))
label3_text.move(680,100)

# set the label fourth for inputs
label4 = QLabel(windows)
label4.setText("Court Name : ")
label4.setFont(QFont("Arial",20))
label4.move(20,190)

# create inputs for the court name
label4_text = QLineEdit(windows)
label4_text.resize(300,50)
label4_text.setFont(QFont('Arial',20))
label4_text.move(250,180)


# set the label fifth for inputs
label5 = QLabel(windows)
label5.setText("Record Room No : ")
label5.setFont(QFont("Arial",20))
label5.move(20,280)

# create inputs five for the record room no
label5_text = QLineEdit(windows)
label5_text.resize(300,50)
label5_text.setFont(QFont('Arial',20))
label5_text.move(250,270)

btn = QPushButton(windows)
btn.setText("Save")
btn.setFont(QFont('Arial',15))
btn.resize(150,50)
btn.move(300,350)



# set the windows size
windows.setGeometry(500,500,1000,1000)

# set the windows Name
windows.setWindowTitle("New Dashboard")

# windows show function
windows.show()

# set click exit to exit windows
sys.exit(app.exec_())
windows()
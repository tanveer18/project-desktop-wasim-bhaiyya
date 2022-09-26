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
label1.setText("Search : ")
label1.setFont(QFont("Arial Bold",20))
label1.move(20,30)

# create inputs first text bar
label1_text = QLineEdit(windows)
label1_text.resize(300,50)
label1_text.setFont(QFont('Arial',20))
label1_text.move(150,20)


# create a button for search
btn = QPushButton(windows)
btn.setText("Search")
btn.resize(120,50)
btn.setFont(QFont('Arial',15))
btn.move(500,20)

# create a radio1 button
radio1 = QRadioButton(windows)
radio1.setText("Name of Parties")
radio1.setFont(QFont('Arial',15))
radio1.move(150,100)


# create a radio2 button
radio2 = QRadioButton(windows)
radio2.setText("Case Number")
radio2.setFont(QFont('Arial',15))
radio2.move(350,100)

# create a radio3 button
radio3 = QRadioButton(windows)
radio3.setText("Court Name")
radio3.setFont(QFont('Arial',15))
radio3.move(150,150)


# create a radio4 button
radio4 = QRadioButton(windows)
radio4.setText("Record Room No")
radio4.setFont(QFont('Arial',15))
radio4.move(350,150)


# create a button for New Record
btn = QPushButton(windows)
btn.setText("New Record")
btn.setFont(QFont('Arial',15))
btn.resize(130,50)
btn.move(150,200)


# create a button for Update Record
btn = QPushButton(windows)
btn.setText("Update Record")
btn.setFont(QFont('Arial',15))
btn.resize(150,50)
btn.move(330,200)

# set the windows size
windows.setGeometry(700,700,1000,1000)

# set the windows Name
windows.setWindowTitle("Home")

# windows show function
windows.show()

# set click exit to exit windows
sys.exit(app.exec_())
windows()
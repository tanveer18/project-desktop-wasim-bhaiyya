import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# create a windows
app = QApplication(sys.argv)

# set the name of windows
windows = QWidget()

# set the label first for user name given label in the windows font setting moving to set windows
label1 = QLabel(windows)
label1.setText("User Name : ")

label1.setFont(QFont("Arial Bold",20))
label1.move(20,30)

# set the text for first edit for user name
label1_text = QLineEdit(windows)
label1_text.resize(300,50)
label1_text.setFont(QFont('Arial',20))
label1_text.move(200,20)

# set the label second for the password
label2 = QLabel(windows)
label2.setText("Password : ")
label2.setFont(QFont("Arial Bold",20))
label2.move(20,100)

# set the second exit text for password
label2_text = QLineEdit(windows)
label2_text.resize(300,50)
label2_text.setFont(QFont('Arial',20))
label2_text.move(200,90)

# create a button for login
btn = QPushButton(windows)
btn.setText("Login")
btn.setFont(QFont('Arial',15))
btn.resize(130,50)
btn.move(270,160)


# set the windows size
windows.setGeometry(700,700,1000,1000)

# set the windows Name
windows.setWindowTitle("Login Dashboard")

# windows show function
windows.show()


# set click exit to exit windows
sys.exit(app.exec_())
windows()

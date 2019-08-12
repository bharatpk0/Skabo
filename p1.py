import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QPixmap, QIcon

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 50, 1500, 900)
        self.setWindowTitle("Skabo")
        self.UI()
        self.show()

    def UI(self):

        self.heading = QLabel(self)
        self.heading.setText("Signin")
        self.heading.setStyleSheet("font:50px;color:#F44D63")
        self.heading.move(1100,150)
        self.btn1 = QPushButton("Let's go", self)
        self.btn1.move(1300, 480)
        self.btn1.resize(100,50)
        self.btn1.setIcon(QIcon(QPixmap("./static/images/login.png")))
        self.btn1.setStyleSheet("background-color:#FF5144 ")
        self.btn1.clicked.connect(self.clickfun)
        self.ulable= QLabel(self)
        self.ulable.setText("Username")
        self.ulable.move(900,310)
        self.ulable.setStyleSheet("font:20px")
        self.plable= QLabel(self)
        self.plable.setText("Password")
        self.plable.move(900,400)
        self.plable.setStyleSheet("font:20px")
        self.username = QLineEdit(self)
        self.username.move(1000, 300)
        self.username.resize(400,50)
        # self.username.set
        self.username.setPlaceholderText("Your Username goes here ...")
        self.password = QLineEdit(self)
        self.password.move(1000, 390)
        self.password.resize(400,50)
        self.password.setPlaceholderText("Your Password goes here ...")
        self.password.setEchoMode(QLineEdit.Password)


        self.image = QLabel(self)
        self.image.setPixmap(QPixmap("./static/images/logo_main.png"))
        self.image.move(0,170)




        self.show()

    def clickfun(self):
        password = self.password.text()
        username = self.username.text()
        # error_dialog = QtWidgets.QErrorMessage()

        if username=="bharat" and password== "asas":
            print("Login")
        else:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Invalid Credentials')
            error_dialog.setWindowTitle("Warning")
            error_dialog.move(1250,300)

            error_dialog.exec_()



def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()

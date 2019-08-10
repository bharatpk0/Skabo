import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 250, 350, 350)
        self.setWindowTitle("Skabo")
        self.UI()
        self.show()

    def UI(self):
        self.btn1 = QPushButton("Login", self)
        self.btn1.move(128, 200)
        self.btn1.clicked.connect(self.clickfun)
        self.username = QLineEdit(self)
        self.username.move(100, 120)
        self.username.set
        self.username.setPlaceholderText("Enter Username")
        self.password = QLineEdit(self)
        self.password.move(100, 160)
        self.password.setPlaceholderText("Enter Password")
        self.password.setEchoMode(QLineEdit.Password)


        self.image = QLabel(self)
        self.image.setPixmap(QPixmap("./static/images/logo.png"))
        self.image.move(50,5)


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
            error_dialog.move(515,350)

            error_dialog.exec_()



def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()

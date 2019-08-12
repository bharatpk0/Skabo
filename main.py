import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QLineEdit, QAction
from PyQt5.QtGui import QPixmap, QIcon


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 50, 1500, 900)
        self.setWindowTitle("Skabo")
        self.UI()
        self.show()

    def UI(self):
        self.toolbar()


        self.show()




    def toolbar(self):
        self.tb = self.addToolbar("Tool bar")
        ############################################
        self.add_product_tool = QAction(QIcon("addprod.png"), "Add Product",self)
        self.tb.addAction(self.add_product_tool)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()

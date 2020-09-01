import sys
from PyQt5.QtWidgets import QDialog, QApplication
from dialog import *


class MainWindow(QDialog):

    def __init__(self):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.display_message)
        self.show()
    
    def display_message(self):

        self.ui.label_1.setText("Hello " + self.ui.lineEdit.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
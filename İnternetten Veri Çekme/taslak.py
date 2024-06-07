from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
import sys

class Pencere(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Live Video")
        self.setGeometry(100, 400, 640, 480)

        self.merkezWidget = QWidget(self)
        self.setCentralWidget(self.merkezWidget)

        self.acButton = QPushButton("Open Live Video", self)
        self.acButton.clicked.connect(self.videoAc)

    def videoAc(self):
        fileName = QFileDialog.getOpenFileName(self, "Open Video")
        if fileName:
            print("Kod calisiyor")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    pencere = Pencere()
    pencere.show()
    sys.exit(app.exec_())


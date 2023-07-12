from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton
import sys
def empyt():
    print("w")
    return 5
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("Push for Window")
        self.setCentralWidget(self.button)

    


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
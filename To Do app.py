from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont


def main():
    app = QApplication([])
    window = QWidget()

    label = QLabel(window)
    label.setText("KawaBanga")
    label.setFont(QFont("Arial", 16))
    window.setGeometry(100, 100, 200, 300)

    window.show()
    app.exec_()


if __name__ == "__main__":
    main()

from PyQt5.QtWidgets import *


def main():
    app = QApplication([])
    window = QWidget()
    window.show()

    label = QLabel(window)
    label.setText("KawaBanga")
    app.exec_()


if __name__ == "__main__":
    main()

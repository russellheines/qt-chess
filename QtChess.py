import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QIcon

from QtBoard import QtBoard


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Let's Play Chess!")
        self.setGeometry(100, 100, 576, 576)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        board = QtBoard()
        central_widget.setLayout(board.grid)

        board.draw()


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("img/logo192.png"))

    screen = app.primaryScreen()
    print('Screen: %s' % screen.name())
    size = screen.size()
    print('Size: %d x %d' % (size.width(), size.height()))
    rect = screen.availableGeometry()
    print('Available: %d x %d' % (rect.width(), rect.height()))

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

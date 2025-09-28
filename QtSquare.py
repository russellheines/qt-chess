from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtSvg import QSvgRenderer

svg_files = {
    'p': 'img/cburnett/pdt45.svg',
    'r': 'img/cburnett/rdt45.svg',
    'n': 'img/cburnett/ndt45.svg',
    'b': 'img/cburnett/bdt45.svg',
    'q': 'img/cburnett/qdt45.svg',
    'k': 'img/cburnett/kdt45.svg',
    'P': 'img/cburnett/plt45.svg',
    'R': 'img/cburnett/rlt45.svg',
    'N': 'img/cburnett/nlt45.svg',
    'B': 'img/cburnett/blt45.svg',
    'Q': 'img/cburnett/qlt45.svg',
    'K': 'img/cburnett/klt45.svg'
}


class QtSquare:
    def __init__(self, board, row, col, piece=None, selected=False):
        self.board = board
        self.row = row
        self.col = col
        self.piece = piece
        self.selected = selected

        self.label = QLabel()
        self.label.setMinimumSize(72, 72)

        if self.row % 2 == self.col % 2:
            # light
            if self.selected and self.selected[0] == self.row and self.selected[1] == self.col:
                self.label.setStyleSheet("background-color: rgb(130, 151, 105);")
            else:
                self.label.setStyleSheet("background-color: rgb(240, 217, 181);")
        else:
            # dark
            if self.selected and self.selected[0] == self.row and self.selected[1] == self.col:
                self.label.setStyleSheet("background-color: rgb(100, 111, 64);")
            else:
                self.label.setStyleSheet("background-color: rgb(181, 136, 99);")

        if self.piece:
            # Create SVG renderer
            svg_renderer = QSvgRenderer(svg_files[piece])

            # Create QPixmap to draw the SVG onto
            # Adjust size as needed
            pixmap = QPixmap(QSize(72, 72))
            pixmap.fill(Qt.transparent)  # Transparent background

            # Draw SVG onto QPixmap
            painter = QPainter(pixmap)
            svg_renderer.render(painter)
            painter.end()

            # Create QLabel and set the pixmap
            self.label.setPixmap(pixmap)

        self.label.mousePressEvent = self.on_click

    def on_click(self, event):
        #print("Clicked row " + str(self.row) + " col " + str(self.col))
        self.board.click_square(self.row, self.col)

from PyQt5.QtWidgets import QGridLayout
import chess
import random

from QtSquare import QtSquare


class QtBoard:
    def __init__(self):
        self.grid = QGridLayout()
        self.grid.setSpacing(0)
        self.grid.setRowStretch(8, 1)
        self.grid.setColumnStretch(8, 1)
        self.selected = None

        self.chess_board = chess.Board()

    def draw(self):
        matrix = [[None for _ in range(8)] for _ in range(8)]
        for row in range(8):
            for col in range(8):
                piece = self.chess_board.piece_at(chess.square(col, 7-row))  # file_index, rank_index
                matrix[row][col] = None if piece is None else piece.symbol()

        for row in range(8):
            for col in range(8):
                label = QtSquare(self, row, col, matrix[row][col], self.selected)
                self.grid.addWidget(label.label, row, col)

    def click_square(self, row, col):
        if self.chess_board.is_checkmate() or self.chess_board.is_stalemate():
            return
        elif not self.selected:
            self.selected = (row, col)
            #print("Selected row " + str(self.selected[0]) + " col " + str(self.selected[1]))
        elif self.selected[0] == row and self.selected[1] == col:
            self.selected = None
        else:
            from_file = chr(97 + self.selected[1])
            from_rank = 8 - self.selected[0]
            to_file = chr(97 + col)
            to_rank = 8 - row
            uci = from_file + str(from_rank) + to_file + str(to_rank)
            if to_rank == 8 and self.chess_board.piece_type_at(chess.square(self.selected[1], 7-self.selected[0])) == chess.PAWN:
                uci = uci + "q"
            #print("Trying " + uci)

            try:
                move = chess.Move.from_uci(uci)
                if move in self.chess_board.legal_moves:
                    self.chess_board.push(move)
            except ValueError:
                print("ValueError trying move " + uci)
            finally:
                self.selected = None

            if self.chess_board.is_checkmate():
                print("Checkmate!")
            elif self.chess_board.is_stalemate():
                print("Slatemate!")
            elif self.chess_board.turn == chess.BLACK:
                random_move = random.choice(list(self.chess_board.legal_moves))
                self.chess_board.push(random_move)

        self.draw()

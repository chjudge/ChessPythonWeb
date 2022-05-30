# abstraction
from abc import ABC, abstractmethod


class Piece(ABC):
    # constructor for abstract
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.hasMoved = False

    # takes in argument move (which has start and end position)
    # checks to see if the piece can move
    @abstractmethod
    def canMove(self, move, board):
        pass

    # when a piece has moved
    def moved(self) -> None:
        self.hasMoved = True

    #changes the row & col for the piece
    def pieceMove(self, row, col):
        self.row = row
        self.col = col

    # toString method (is abstract)
    @abstractmethod
    def __str__(self):
        pass

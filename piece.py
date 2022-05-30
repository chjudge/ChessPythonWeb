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

    # getter methods
    def get_col(self):
        return self.col

    def get_row(self):
        return self.row

    def getColor(self):
        return self.color

    def hasMoved(self):
        return self.hasMoved

    # toString method (is abstract)
    @abstractmethod
    def __str__(self):
        pass

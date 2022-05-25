# abstraction
from abc import ABC, abstractmethod
class Piece(ABC):
    # constructor for abstract
    def __init__(self, yPos, xPos, color):
        self.yPos = yPos
        self.xPos = xPos
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
    def getX(self):
        return self.xPos
    def getY(self):
        return self.yPos
    def getColor(self):
        return self.color
    def hasMoved(self):
        return self.hasMoved

    # toString method (is abstract)
    @abstractmethod
    def __str__(self):
        pass
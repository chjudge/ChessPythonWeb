# abstraction
from abc import ABC, abstractmethod
from xmlrpc.client import Boolean
class Piece(ABC):
    # constructor for abstract
    def __init__(self, xPos, yPos, color):
        self.xPos = xPos
        self.yPos = yPos
        self.color = color
        self.hasMoved = False

    # takes in argument move (which has start and end position)
    # checks to see if the piece can move
    @abstractmethod
    def canMove(self, move) -> Boolean:
        pass

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
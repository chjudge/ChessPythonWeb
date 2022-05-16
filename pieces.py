from abc import ABC
class Pieces(ABC):
    # print("Hi")
    def __init__(self, xPos, yPos, color):
        self.xPos = xPos
        self.yPos = yPos
        self.color = color
        self.hasMoved = False
    # abstract function for the movment o each type of piece
    def canMove(self, move):
        pass
    # checks to see if piece can move
    # takes in argument move (which has start and end position)
    def pieceInWay(self, move):
        return False

    # getter methods
    def getX(self):
        return self.xPos
    def getY(self):
        return self.yPos
    def getColor(self):
        return self.color
    def hasMoved(self):
        return self.hasMoved

from shutil import move


class Move():
    def __init__(self):
        self.startPosR = None
        self.startPosC = None
        self.endPosR = None
        self.endPosC = None

    # Setter Method
    # moveNotation is a string that will be converted into a the move variables 
    # Chess move notation is as follows: [pieceLocation]-[pieceDestination] ex.) b1-a3 *knight move
    def setMove(self, moveNotation): 
        self.startPosC = "abcdefgh".index(moveNotation[0])
        self.startPosR = self.invertRowNums((int)(moveNotation[1]) - 1)
        self.endPosC = "abcdefgh".index(moveNotation[3])
        self.endPosR = self.invertRowNums((int)(moveNotation[4]) - 1)

    # this is needed because the board is printed with 0 at the top not 7
    def invertRowNums(self, rowVal):
        return abs(rowVal - 7)


    # Getter Methods
    def getStartR(self):
        return self.startPosR
    def getStartC(self):
        return self.startPosC
    def getEndR(self):
        return self.endPosR
    def getEndC(self):
        return self.endPosC

    
    print("HI")

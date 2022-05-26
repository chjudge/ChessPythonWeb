from piece import Piece as p
from empty import Empty

class Rook(p):
    # Constuctor defined in parents

    # defining the canMove method: involves defining how the piece moves
    def canMove(self, move, board):
        endR = move.getEndR()
        endC = move.getEndC()
        if((endR == self.getY() and endC == self.getX()) or
            (self.getY() != endR and self.getX() != endC)):
            print("1")
            return False
        color = self.getColor()  
        
        # checks horizontal or vertical
        # then checks to make sure there are no pieces in the way & the end square is the right color
        if(self.getY() != endR):
            minVal = min(self.getY(), endR)
            maxVal = max(self.getY(), endR)
            for diff in range(1,maxVal - minVal):
                if(not isinstance(board[minVal + diff][endC], Empty)):
                    print("2")
                    return False
            if(board[endR][endC].getColor() == color):
                print("3")
                return False
            print("vertical movment")
        else:
            minVal = min(self.getX(), endC)
            maxVal = max(self.getX(), endC)
            for diff in range(1, maxVal - minVal):
                if(not isinstance(board[endR][minVal + diff], Empty)):
                    print("4")
                    return False
            if(board[endR][endC].getColor() == color):
                print("5")
                return False
            print("horizontal movement")
        return True

    def __str__(self):
        return " R "
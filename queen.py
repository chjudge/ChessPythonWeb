from piece import Piece as p
from empty import Empty

class Queen(p):
    # Constuctor defined in parents

    # defining the canMove method: involves defining how the piece moves
    def canMove(self, move, board):
        endR = move.end_row
        endC = move.end_col
        startR = self.row
        startC = self.col
        
        # general parameter check
        if((endR == startR and endC == startC) or 
            (abs(startR - endR) != abs(startC - endC) and (endR != startR and endC != startC) )):
            return False

        # this checks how the piece is moving (horizontal, vertical, or diagnol)
        # then checks if a piece is in the way
        HORIZONTAL = 0
        VERTICAL = 0 
        if(startR != endR):
            VERTICAL = (startR - endR)/abs(endR - startR)
        if(startC != endC):
            HORIZONTAL = (endC - startC)/abs(endC - startC)

        for diff in range(1,abs(startR - endR)):
            if(not isinstance(board.getPiece((int)(startR - diff * VERTICAL), (int)(startC + diff * HORIZONTAL)), Empty)):
                print("1")
                return False
        if(board.getPiece(endR, endC).color == self.color):
            print("2")
            return False
        return True

    def __str__(self):
        return " Q "
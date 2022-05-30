from piece import Piece as p
from empty import Empty

class Bishop(p):
    # Constuctor defined in parents

    # defining the canMove method: involves defining how the piece moves
    def canMove(self, move, board):
        endR = move.end_row
        endC = move.end_col
        startR = self.row
        startC = self.col
        # general parameter check
        if(endR == startR or endC == startC or abs(startR - endR) != abs(startC - endC)):
            return False
        
        # figures out the direction of the piece
        # then checks to make sure there are no pieces in the way
        VERTICAL = (startR - endR)/abs(endR - startR)
        HORIZONTAL = (endC - startC)/abs(endC - startC)
        for diff in range(1,abs(startR - endR)):
            if(not isinstance(board.getPiece((int)(startR - diff * VERTICAL), (int)(startC + diff * HORIZONTAL)), Empty)):
                return False
        if(board.getPiece(endR, endC).color == self.color):
            return False
        return True

    def __str__(self):
        return " B "
    
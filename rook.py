from piece import Piece as p
from empty import Empty

class Rook(p):
    # Constuctor defined in parents

    # defining the canMove method: involves defining how the piece moves
    def canMove(self, move, board):
        endR = move.end_row
        endC = move.end_col
        startR = self.row
        startC = self.col
        # general parameter check
        if((endR == startR and endC == startC) or
            (startR != endR and startC != endC)):
            return False
        
        # checks horizontal or vertical
        # then checks to make sure there are no pieces in the way & the end square is the right color
        HORIZONTAL = 0
        VERTICAL = 0 
        if(startC == endC):
            VERTICAL = (startR - endR)/abs(endR - startR)
        else:
            HORIZONTAL = (endC - startC)/abs(endC - startC)
        for diff in range(1,abs(startR - endR)):
            if(not isinstance(board.getPiece((int)(startR - diff * VERTICAL), (int)(startC + diff * HORIZONTAL))], Empty)):
                return False
        if(board.getPiece(endR, endC).color == self.color):
            return False
        return True

        # PHASE 2 ------------------------------------

        # HORIZONTAL = 0
        # VERTICAL = 0
        # if(startR == endR):
        #     minVal = min(startC, endC)
        #     maxVal = max(startC, endC)
        #     HORIZONTAL = 1
        # else:
        #     minVal = min(startR, endR)
        #     maxVal = max(startR, endR)
        #     VERTICAL = 1        
        # # since board[row][col] uses minimal value, row can be added to (rather than subtracted)
        # for diff in range(1,maxVal - minVal):
        #     if( not isinstance(board
        #         [endR * HORIZONTAL + (minVal + diff)  * VERTICAL]
        #         [endC * VERTICAL + (minVal + diff) * HORIZONTAL], Empty)
        #     ):
        #         return False
        # if(board.getPiece(endR, endC).color == self.color):
        #     return False
        # return True

        # PHASE 1 ------------------------------------

        # HORIZONTAL = 0
        # VERTICAL = 0
        # if(self.getY() != endR):
        #     minVal = min(self.getY(), endR)
        #     maxVal = max(self.getY(), endR)
        #     for diff in range(1,maxVal - minVal):
        #         if(not isinstance(board[minVal + diff][endC], Empty)):
        #             print("2")
        #             return False
        #     if(board.getPiece(endR, endC).color == color):
        #         print("3")
        #         return False
        #     print("vertical movment")
        # else:
        #     minVal = min(self.getX(), endC)
        #     maxVal = max(self.getX(), endC)
        #     for diff in range(1, maxVal - minVal):
        #         if(not isinstance(board[endR][minVal + diff], Empty)):
        #             print("4")
        #             return False
        #     if(board.getPiece(endR, endC).color == color):
        #         print("5")
        #         return False
        #     print("horizontal movement")
        # return True

    def __str__(self):
        return " R "
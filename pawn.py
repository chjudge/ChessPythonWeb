from piece import Piece as p
from empty import Empty

class Pawn(p):
    # Constuctor defined in parents

    # defining the canMove method: involves defining how the piece moves
    def canMove(self, move, board):
        endR = move.end_row
        endC = move.end_col
        color = self.color
        
        # up-2, up1, take diagnol, en passant, false
        if(
            isinstance(board.getPiece(endR, endC), Empty) and
            self.hasMoved == False and 
            self.col == endC and
            ((color == "white" and endR == 4) or (color == "black" and endR == 3))
        ):
            return True
        elif(
                isinstance(board.getPiece(endR, endC), Empty) and
                self.col == endC and
                (color == "white" and endR == self.row - 1) or
                (color == "black" and endR == self.row + 1)):
            return True
        elif(
                board.getPiece(endR, endC).color != "n/a" and
                board.getPiece(endR, endC).color != color and
                (self.col + 1 == endC or self.col - 1 == endC) and
                ((color == "white" and endR == self.row - 1) or
                 (color == "black" and endR == self.row + 1))
        ):
            return True
        #elif (en passant is true): return True
        return False

    def __str__(self):
        return " P "
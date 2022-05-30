from piece import Piece as p
from empty import Empty

class Pawn(p):
    # Constuctor defined in parents

    # defining the canMove method: involves defining how the piece moves
    def canMove(self, move, board):
        endR = move.getEndR()
        endC = move.getEndC()
        color = self.getColor()
        
        # up-2, up1, take diagnol, en passant, false
        if(
            isinstance(board[endR][endC], Empty) and
            self.hasMoved == False and 
            self.get_col() == endC and
            ((color == "white" and endR == 4) or (color == "black" and endR == 3))
        ):
            return True
        elif(
                isinstance(board[endR][endC], Empty) and
                self.get_col() == endC and
                (color == "white" and endR == self.get_row() - 1) or
                (color == "black" and endR == self.get_row() + 1)):
            return True
        elif(
                board[endR][endC].getColor() != "n/a" and
                board[endR][endC].getColor() != color and
                (self.get_col() + 1 == endC or self.get_col() - 1 == endC) and
                ((color == "white" and endR == self.get_row() - 1) or
                 (color == "black" and endR == self.get_row() + 1))
        ):
            return True
        #elif (en passant is true): return True
        return False

    def __str__(self):
        return " P "
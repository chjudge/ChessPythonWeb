from piece import Piece as p
import math
 
class King(p):
    # Constuctor defined in parents

    # defining the canMove method: involves defining how the piece moves
    def canMove(self, move, board):
        endR = move.getEndR()
        endC = move.getEndC()
        startR = self.getY()
        startC = self.getX()

        # general parameter check
        # uses distance formula to check if the move is legal
        if(endR == startR and endC == startC):
            return False

        distance = math.sqrt(math.pow(startR - endR,2) + math.pow(startC - endC,2))

        if((distance != 1 and distance != math.sqrt(2)) or
            board[endR][endC].getColor() == self.getColor()):
            return False
        return True

    def __str__(self):
        return " K "
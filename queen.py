from piece import Piece as p

class Queen(p):
    # Constuctor defined in parents

    # defining the canMove method: involves defining how the piece moves
    def canMove(self, move, board):
        endR = move.getEndR()
        endC = move.getEndC()
        startR = self.getY()
        startC = self.getX()
        # general parameter check
        if((endR == startR and endC == startC) or 
            (abs(startR - endR) != abs(startC - endC) and (endR != startR or endC != startC) )):
            return False
        
        print(endR == startR and endC == startC)
        print(f"{abs(startR - endR) != abs(startC - endC)} and {endR == startR or endC == startC}")

        return True

    def __str__(self):
        return " Q "
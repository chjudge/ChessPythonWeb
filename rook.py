from piece import Piece as p

class Rook(p):
    # Constuctor defined in parents

    # defining the canMove method: involves defining how the piece moves
    def canMove(self, nove):
        print("Rook can move")

    def __str__(self):
        return " R "
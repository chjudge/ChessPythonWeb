from piece import Piece as p

class Pawn(p):
    # Constuctor defined in parents

    # defining the canMove method: involves defining how the piece moves
    def canMove(self, nove):
        print("Pawn can move")
        return True

    def __str__(self):
        return " P "
from piece import Piece as p

class Bishop(p):
    # Constuctor defined in parents

    # defining the canMove method: involves defining how the piece moves
    def canMove(self, nove):
        print("Bishop can move")

    def __str__(self):
        return " B "
    
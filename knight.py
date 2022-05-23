from piece import Piece as p

class Knight(p):
    # Constuctor defined in parents

    # defining the canMove method: involves defining how the piece moves
    def canMove(self, nove):
        print("Knight can move")

    def __str__(self):
        return "Kn "

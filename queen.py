from piece import Piece as p

class Queen(p):
    # Constuctor defined in parents

    # defining the canMove method: involves defining how the piece moves
    def canMove(self, nove):
        # print("Queen can move")
        return False

    def __str__(self):
        return " Q "
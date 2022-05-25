from piece import Piece as p

class Bishop(p):
    # Constuctor defined in parents

    # defining the canMove method: involves defining how the piece moves
    def canMove(self, move, board):
        # print("Bishop can move")
        return False

    def __str__(self):
        return " B "
    
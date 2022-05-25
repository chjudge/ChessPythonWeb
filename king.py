from piece import Piece as p
 
class King(p):
    # Constuctor defined in parents

    # defining the canMove method: involves defining how the piece moves
    def canMove(self, move, board):
        # print("King can move")
        return False

    def __str__(self):
        return " K "
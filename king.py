from piece import Piece as p
 
class King(p):
    # Constuctor defined in parents

    # defining the canMove method: involves defining how the piece moves
    def canMove(self, nove):
        print("King can move")

    def __str__(self):
        return " K "
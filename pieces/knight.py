from pieces.piece import Piece
import math


class Knight(Piece):
    # Constructor defined in parents

    # defining the canMove method: involves defining how the piece moves
    def can_move(self, move, board):
        endR = move.end_row
        endC = move.end_col
        startR = self.row
        startC = self.col

        # general parameter check
        # uses distance formula to check if the move is legal
        if endR == startR and endC == startC:
            return False

        if (math.sqrt(math.pow(startR - endR, 2) + math.pow(startC - endC, 2)) != math.sqrt(5) or
                board.get_piece(endR, endC).color == self.color):
            return False

        return True

    def __str__(self):
        return "Kn "

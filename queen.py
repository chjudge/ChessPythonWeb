from piece import Piece as p
from empty import Empty


class Queen(p):
    # Constructor defined in parents

    # defining the canMove method: involves defining how the piece moves
    def can_move(self, move, board):
        endR = move.end_row
        endC = move.end_col
        startR = self.row
        startC = self.col

        # general parameter check
        if ((endR == startR and endC == startC) or
                (abs(startR - endR) != abs(startC - endC) and (endR != startR and endC != startC))):
            return False

        # this checks how the piece is moving (horizontal, vertical, or diagnose)
        # then checks if a piece is in the way
        HORIZONTAL = 0
        VERTICAL = 0
        if startR != endR:
            VERTICAL = (startR - endR) / abs(endR - startR)
        if startC != endC:
            HORIZONTAL = (endC - startC) / abs(endC - startC)

        for diff in range(1, abs(startR - endR)):
            if not isinstance(board.get_piece(int(startR - diff * VERTICAL), int(startC + diff * HORIZONTAL)), Empty):
                print("1")
                return False
        if board.get_piece(endR, endC).color == self.color:
            print("2")
            return False
        return True

    def __str__(self):
        return " Q "

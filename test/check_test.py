from board import Board
from move import Move
from pieces.empty import Empty
from pieces.rook import Rook
from pieces.king import King
from pieces.pawn import Pawn
from pieces.queen import Queen

def testBishopCheck():
    board = Board()
    move = Move()
    move.define_move(1, 5, 3, 5)
    board.move_piece(move, True)
    # move.define_move(7, 4, 6, 4)
    # board.move_piece(move, False)
    # move.define_move(1, 6, 5, 2)
    # board.move_piece(move, True)
    print(board)
    assert board.get_piece(5, 7).vulnerable(5, 7, board)


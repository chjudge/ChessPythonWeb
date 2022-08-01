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
    move.define_move(6, 4, 4, 4)
    board.move_piece(move, True)
    move.define_move(1, 3, 2, 3)
    board.move_piece(move, False)
    move.define_move(7, 5, 3, 1)
    board.move_piece(move, True)
    print(board)
    assert board.get_piece(0, 4).king_check(0, 4, board)

def testRookCheck():
    board = Board()
    move = Move()
    move.define_move(6, 0, 4, 0)
    board.move_piece(move, True)
    move.define_move(7, 0, 5, 0)
    board.move_piece(move, True)
    move.define_move(5, 0, 5, 4)
    board.move_piece(move, True)
    move.define_move(5, 4, 1, 4)
    board.move_piece(move, True)
    print(board)
    assert board.get_piece(0, 4).king_check(0, 4, board)

def testKnightCheck():
    board = Board()
    move = Move()
    move.define_move(7, 1, 5, 2)
    board.move_piece(move, True)
    move.define_move(5, 2, 3, 1)
    board.move_piece(move, True)
    move.define_move(3, 1, 1, 2)
    board.move_piece(move, True)
    print(board)
    assert board.get_piece(0, 4).king_check(0, 4, board)

def testQueenCheck():
    board = Board()
    move = Move()
    move.define_move(6, 4, 5, 4)
    board.move_piece(move, True)
    move.define_move(7, 3, 4, 6)
    board.move_piece(move, True)
    move.define_move(7, 5, 3, 1)
    board.move_piece(move, True)
    move.define_move(4, 6, 1, 3)
    board.move_piece(move, True)
    print(board)
    assert board.get_piece(0, 4).king_check(0, 4, board)
    move.define_move(0, 3, 1, 3)
    board.move_piece(move, False)
    print(board)
    assert board.get_piece(0, 4).king_check(0, 4, board) == False


from board import Board
from move import Move
from pieces.empty import Empty
from pieces.rook import Rook
from pieces.king import King
from pieces.pawn import Pawn
from pieces.queen import Queen


def test_bishop_check():
    board = Board()
    move = Move()
    move.define_move(6, 4, 4, 4)
    board.move_piece(move, True)
    move.define_move(1, 3, 2, 3)
    board.move_piece(move, False)
    move.define_move(7, 5, 3, 1)
    board.move_piece(move, True)
    print(board)
    assert board.in_check(False)
    # assert board.get_piece(0, 4).can_move(0, 4, board)


def test_rook_check():
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
    assert board.in_check(False)


def test_knight_check():
    board = Board()
    move = Move()
    move.define_move(7, 1, 5, 2)
    board.move_piece(move, True)
    move.define_move(5, 2, 3, 1)
    board.move_piece(move, True)
    move.define_move(3, 1, 1, 2)
    board.move_piece(move, True)
    print(board)
    assert board.in_check(False)


def test_queen_check():
    board = Board()
    move = Move()
    move.define_move(6, 4, 5, 4)
    board.move_piece(move, True)
    move.define_move(7, 3, 4, 6)
    board.move_piece(move, True)
    # move.define_move(7, 5, 3, 1)
    # board.move_piece(move, True)
    move.define_move(4, 6, 1, 3)
    board.move_piece(move, True)
    print(board)
    assert board.in_check(False)
    move.define_move(0, 3, 1, 3)
    board.move_piece(move, False)
    print(board)
    print(f"{board.in_check(False)} is the state of board for check")
    assert board.in_check(False) == None


def test_checkmate1():
    board = Board()
    move = Move()
    move.define_move(6, 5, 5, 5)
    board.move_piece(move, True)
    move.define_move(1, 4, 2, 4)
    board.move_piece(move, False)
    move.define_move(6, 6, 4, 6)
    board.move_piece(move, True)
    move.define_move(0, 3, 4, 7)
    board.move_piece(move, False)
    print(board)
    assert board.in_checkmate(True)


def test_checkmate2():
    board = Board()
    move = Move()
    move.define_move(6, 4, 5, 4)
    board.move_piece(move, True)
    move.define_move(1, 3, 2, 3)
    board.move_piece(move, False)
    move.define_move(7, 3, 4, 6)
    board.move_piece(move, True)
    move.define_move(0, 3, 1, 3)
    board.move_piece(move, False)
    move.define_move(7, 5, 3, 1)
    board.move_piece(move, True)
    move.define_move(1, 3, 3, 1)
    board.move_piece(move, False)
    move.define_move(4, 6, 0, 2)
    board.move_piece(move, True)
    print(board)
    assert board.in_check(False)
    assert board.in_checkmate(False)


def test_checkmate3():
    board = Board()
    move = Move()
    move.define_move(6, 5, 5, 5)
    board.move_piece(move, True)
    move.define_move(1, 4, 2, 4)
    board.move_piece(move, False)
    move.define_move(6, 6, 4, 6)
    board.move_piece(move, True)
    move.define_move(6, 7, 4, 7)
    board.move_piece(move, True)
    move.define_move(4, 7, 3, 7)
    board.move_piece(move, True)
    move.define_move(7, 7, 4, 7)
    board.move_piece(move, True)
    move.define_move(0, 3, 4, 7)
    board.move_piece(move, False)
    print(board)
    assert board.in_checkmate(True)

def test_not_checkmate():
    board = Board()
    move = Move()
    move.define_move(6, 5, 5, 5)
    board.move_piece(move, True)
    move.define_move(1, 4, 2, 4)
    board.move_piece(move, False)
    move.define_move(6, 6, 4, 6)
    board.move_piece(move, True)
    move.define_move(6, 7, 4, 7)
    board.move_piece(move, True)
    move.define_move(4, 7, 3, 7)
    board.move_piece(move, True)
    print(board)
    assert board.in_checkmate(True) == False

def test_stalemate():
    board = Board()
    move = Move()
    move.define_move(6, 4, 5, 4)
    board.move_piece(move, True)
    move.define_move(1, 0, 3, 0)
    board.move_piece(move, False)
    #-------------------
    move.define_move(7, 3, 3, 7)
    board.move_piece(move, True)
    move.define_move(0, 0, 2, 0)
    board.move_piece(move, False)
    #-------------------
    move.define_move(3, 7, 3, 0)
    board.move_piece(move, True)
    move.define_move(1, 7, 3, 7)
    board.move_piece(move, False)
    #-------------------
    move.define_move(6, 7, 4, 7)
    board.move_piece(move, True)
    move.define_move(2, 0, 2, 7)
    board.move_piece(move, False)
    #-------------------
    move.define_move(3, 0, 1, 2)
    board.move_piece(move, True)
    move.define_move(1, 5, 2, 5)
    board.move_piece(move, False)
    #-------------------
    move.define_move(1, 2, 1, 3)
    board.move_piece(move, True)
    move.define_move(0, 4, 1, 5)
    board.move_piece(move, False)
    print("HERE")
    #-------------------
    move.define_move(1, 3, 1, 1)
    board.move_piece(move, True)
    move.define_move(0, 3, 5, 3)
    board.move_piece(move, False)
    #-------------------
    move.define_move(1, 1, 0, 1)
    board.move_piece(move, True)
    move.define_move(5, 3, 1, 7)
    board.move_piece(move, False)
    #-------------------
    move.define_move(0, 1, 0, 2)
    board.move_piece(move, True)
    move.define_move(1, 5, 2, 6)
    board.move_piece(move, False)
    #-------------------
    move.define_move(0, 2, 2, 4)
    board.move_piece(move, True)
    #-------------------
    # move.define_move(5, 4, 4, 4)
    # board.move_piece(move, True)
    # move.define_move(6, 3, 4, 3)
    # board.move_piece(move, True)

    print(board)
    assert board.in_stalemate(False)
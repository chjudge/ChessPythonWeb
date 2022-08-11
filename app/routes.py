from app import app
from flask import render_template, session, redirect, url_for, request, flash
import secrets
from board import Board
from move import Move

@app.get('/')
def index():
    return redirect(url_for('get_new_game'))


@app.get('/new_game/')
def get_new_game():
    key = secrets.token_hex(16)
    session['board_key'] = key
    app.boards[key] = Board()
    app.moves[key] = Move()
    app.WTM[key] = True
    return redirect(url_for('get_board'))


@app.get('/board/')
def get_board():
    if session.get('board_key') not in app.boards:
        return redirect(url_for('get_new_game'))
    return render_template('board.html')

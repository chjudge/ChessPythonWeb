from app import app
from flask import render_template, request, redirect, url_for, flash


@app.get('/')
def index():
    return render_template('index.html')
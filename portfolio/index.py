#!/usr/bin/python3
"""flask homepage for birthday celebration app"""

from flask import Flask, Blueprint, render_template, request, redirect, url_for
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def index():
    """logics for the homepage"""
    date = datetime.now().strftime("%y-%m-%d %H:%M:%S")
    
    return render_template('index/home.html', date=date)

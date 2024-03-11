#!/usr/bin/python3
"""flask homepage for birthday celebration app"""

from flask import flash, Blueprint, render_template, request, redirect, url_for
from datetime import datetime

birthday_bp = Blueprint("birthday", __name__, url_prefix="/birthday")

@birthday_bp.route('/')
def index():
    """logics for the homepage"""
    current_date = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
    
    return render_template(
        'birthday/home.html', 
        current_date=current_date,
        )

@birthday_bp.route('/photo-gallery')
def photo_gallery():
    """logics for the photo gallery"""
    photos = []
    return render_template(
        'birthday/photo_gallery.html',
        photos=photos
    )

@birthday_bp.route('/message', methods=['GET', 'POST'])
def message():
    """logics for the messages"""
    error = None
    success = ''
    if request.method == 'POST':
        message = request.form.get('message')
        sender = request.form.get('sender')
        word_count = len(message.split())
        if word_count < 3:
            error = 'Haba! Your message is too short for the celebrant. Please enter a message with at least 3 words'
            flash(error, 'error')
            return redirect(url_for('birthday.index', _anchor='send-message'))
        elif word_count > 50:
            error = 'Haba! Your message is too long. Please enter a message with at most 50 words'
            flash(error, 'error')
            return redirect(url_for('birthday.index', _anchor='send-message'))
        else:
            success ='Your message has been sent successfully'
            flash(success, 'success')
    return render_template(
        'birthday/home.html',
        error=error,
        success=success
        )

@birthday_bp.route('/secret-message', methods=['GET', 'POST'])
def secret_message():
    """logics for the secret message"""
    message = ''
    error = None
    success = ''
    if request.method == 'POST':
        message = request.form.get('message')
        word_count = len(message.split())
        if word_count < 3:
            error = 'Haba! Your message is too short for the celebrant. Please enter a message with at least 3 words'
            flash(error, 'error')
            return redirect(url_for('birthday.secret_message', _anchor='secret-message'))
        elif word_count > 50:
            error = 'Haba! Your message is too long. Please enter a message with at most 100 words'
            flash(error, 'error')
            return redirect(url_for('birthday.secret_message', _anchor='secret-message'))
        else:
            success ='Your message has been sent successfully'
            flash(success, 'success')

    return render_template(
        'birthday/secret_message.html',
        message=message,
        error=error,
        success=success
        )

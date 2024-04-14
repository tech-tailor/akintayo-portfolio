#!/usr/bin/python3
"""flask homepage for birthday celebration app"""

from flask import flash, Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from portfolio.models import Message, SecretMessage
from portfolio.database import session

birthday_bp = Blueprint("birthday", __name__, url_prefix="/birthday")

@birthday_bp.route('/photo-gallery')
def photo_gallery():
    """logics for the photo gallery"""
    photos = []
    return render_template(
        'birthday/photo_gallery.html',
        photos=photos
    )

@birthday_bp.route('/', methods=['GET', 'POST'])
def index():
    """logics for the messages"""
    error = None
    success = ''
    messages = ''
    if request.method == 'POST':
        message = request.form.get('message')
        sender = request.form.get('sender')
        word_count = len(message.split())
        sender_names = sender.split()
        
        if word_count < 3:
            error = 'Haba! Your message is too short for the celebrant. Please enter a message with at least 3 words'
            flash(error, 'error')
            return redirect(url_for('birthday.index', _anchor='send-message'))
        elif word_count > 100:
            error = 'Haba! Your message is too long. Please enter a message with at most 100 words'
            flash(error, 'error')
            return redirect(url_for('birthday.index', _anchor='send-message'))
        else:
            success ='Your message has been sent successfully'
            flash(success, 'success')
        if 'from' in sender_names:
            error = 'Do not add the word "from", just your name only'
            flash(error, 'error')
            return redirect(url_for('birthday.index', _anchor='send-message'))
        # Save the user message to the databse
        instance = Message(message=message, sender=sender)
        session.add(instance)   
        session.commit()

    messages = session.query(Message).order_by(Message.id.desc()).limit(5)
    return render_template(
        'birthday/home.html',
        error=error,
        success=success,
        messages=messages,
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
        print('url-------', request.full_path)
        if word_count < 3:
            error = 'Haba! Your message is too short for the celebrant. Please enter a message with at least 3 words'
            flash(error, 'error')
            return redirect(url_for('birthday.secret_message', _anchor='secret-message'))
        elif word_count > 100:
            error = 'Haba! Your message is too long. Please enter a message with at most 100 words'
            flash(error, 'error')
            return redirect(url_for('birthday.secret_message', _anchor='secret-message'))
        else:
            success ='Your message has been sent successfully'
            flash(success, 'success')

        # Save the user message to the database
        instance = SecretMessage(message=message)
        session.add(instance)   
        session.commit()

    secret_messages = session.query(SecretMessage).order_by(SecretMessage.id.desc()).all()
    for msg in secret_messages:
        print(msg)

    return render_template(
        'birthday/secret_message.html',
        message=message,
        error=error,
        success=success
        )


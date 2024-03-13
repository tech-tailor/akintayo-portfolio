#!/usr/bin/python3
"""
Admin logic for Akintayo portfollio"""

from flask import flash, Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from portfolio.models import Message, SecretMessage
from portfolio.database import session

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")
"""Logic for the admin dashboard"""

@admin_bp.route('/', methods=['GET', 'POST'])
def index():
    """Homepage for the admin"""

    # Get all the birthday messages
    messages = session.query(Message).order_by(Message.id.desc()).all()
    return render_template('admin/home.html', messages=messages)

@admin_bp.route('/delete/<string:message_id>', methods=['GET'])
def delete_message(message_id):
    """Delete a message"""
    message = session.query(Message).filter(Message.id == message_id).first()
    objs = session.query(Message).all()
    print('type message_id', type(message_id))
    for obj in objs:
        print(type(obj.id))
        if obj.id == message_id:
            print('obj', obj)
            print('message', message)
    if message:
        session.delete(message)
        print('deleted')
        session.commit()
        flash('Message deleted successfully', 'success')
        return redirect(url_for('admin.birthday_messages'))
    secret_message = session.query(SecretMessage).filter(SecretMessage.id == message_id).first()
    if secret_message:
        session.delete(secret_message)
        session.commit()
        flash('Message deleted successfully', 'success')
        return redirect(url_for('admin.secret_messages'))

@admin_bp.route('/birthday-messages', methods=['GET', 'POST'])
def birthday_messages():
    """Birthday messages"""

    error = 'No messages yet'
    # Get all the birthday messages
    messages = session.query(Message).order_by(Message.id.desc()).all()
    if messages:
        return render_template('admin/birthday_messages.html', messages=messages)
    else:
        return render_template('admin/birthday_messages.html', error=error)

@admin_bp.route('/secret-messages', methods=['GET', 'POST'])
def secret_messages():
    """Secret messages"""

    error = 'No messages yet'
    # Get all the birthday messages
    messages = session.query(SecretMessage).order_by(SecretMessage.id.desc()).all()
    if messages:
        return render_template('admin/secret_messages.html', messages=messages)
    else:
        return render_template('admin/secret_messages.html', error=error)

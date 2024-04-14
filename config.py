#!/usr/bin/python3
"""Config file for the birthday app"""

class Config(object):
    TESTING = False

class DevelopmentConfig(Config):
    """Base config class"""
    DEBUG = True
    PORT= 7000
    SECRET_KEY = 'ffkdgvhgfrjjr876456784y5hnjhgfuy85hk5897fopfjf00939394ldfkjv'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///portfolio.db'
    MAIL_SERVER = 'smtp.example.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'your_email@example.com'
    MAIL_PASSWORD = 'your_email_password'

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

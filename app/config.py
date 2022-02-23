import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', '07YM~7qMKu?[*Ua_u*4M')
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'admin')
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'Password123')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
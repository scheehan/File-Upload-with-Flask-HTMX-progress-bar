import os
from flask import Flask, flash

UPLOAD_FOLDER = '/var/www-flask/static/uploads'

def get_files():
    get_file_filename = os.listdir(UPLOAD_FOLDER)
    return get_file_filename
from flask import Flask
from view import view_app
from auth import auth_app
import os

UPLOAD_FOLDER = "/.files"
app = Flask(__name__)
app.secret_key = str(os.urandom(10))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.register_blueprint(view_app)
app.register_blueprint(auth_app , url_prefix="/auth")


from flask import Flask
from .config import Config
from flask_login import LoginManager
# from flask_uploads import configure_uploads, IMAGES, UploadSet

app = Flask(__name__)
app.config.from_object(Config)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
from app import views

# images = UploadSet('images', IMAGES)
# configure_uploads(app, images)
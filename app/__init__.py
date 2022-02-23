from flask import Flask
from .config import Config
# from flask_uploads import configure_uploads, IMAGES, UploadSet

app = Flask(__name__)
app.config.from_object(Config)
from app import views

# images = UploadSet('images', IMAGES)
# configure_uploads(app, images)
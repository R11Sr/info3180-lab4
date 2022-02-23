from flask_wtf import FlaskForm
# from flask_uploads import UploadSet, IMAGES
from flask_wtf.file import FileField,FileRequired,FileAllowed

# images = UploadSet('images',IMAGES)


class UploadForm(FlaskForm):
    photo = FileField('photo',validators=[FileRequired(),FileAllowed(['jpg', 'png'],'Select Image Files only.')])


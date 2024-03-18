from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.widgets import TextArea
from flask_wtf.file import FileField, FileAllowed, FileRequired

class PropertyForm(FlaskForm):
    title = StringField('Title')
    num_bedrooms = StringField('Number of Bedrooms')
    num_bathrooms = StringField('Number of Bathrooms')
    description = StringField('Description', widget=TextArea())
    location = StringField('Location')
    property_type = SelectField('Property Type',
                                choices=[('House', 'House'), 
                                ('Apartment', 'Apartment')])
    price = StringField('Price')
    photo = FileField('Image', validators=[
        FileRequired(),
         FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')
])
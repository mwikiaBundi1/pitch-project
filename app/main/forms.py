from flask_wtf import FlaskForm
from wtforms import SubmitField, PasswordField, StringField, SelectField,TextAreaField
from wtforms.validators import Required

class InForm(FlaskForm):
    inform = TextAreaField('iNFORM')
    title = StringField('Title')
    category = SelectField(u'Ford category', choices=[('life', 'life', ('code', 'code' ('funny', 'funny')))])
    submit = SubmitField('submit')


class lamentform(FlaskForm):
    comment = TextAreaField('lament')
    submit = SubmitField('Post lamentations')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('What is interesting about you', validators=[Required()])
    submit = SubmitField('submit')
    
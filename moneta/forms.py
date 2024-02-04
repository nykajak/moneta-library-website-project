from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,RadioField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class MyRegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=5,max=20)])
    email = StringField('Email',validators=[DataRequired(),Email(message="Please provide valid email!")])
    password = PasswordField('Password',validators=[DataRequired(),Length(min = 6,max=60)])
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),Length(min = 6,max=60),EqualTo('password',message="Password and confirm password should match!")])
    submit = SubmitField('Sign Up')

class MyLoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email(message="Please provide valid email!")])
    password = PasswordField('Password',validators=[DataRequired(),Length(min = 6,max=60)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class UserSearchForm(FlaskForm):
    book_name = StringField('Book Name')
    author_name = StringField('Author Name')
    section_name = StringField('Genre')
    submit = SubmitField('Search')

class LibrarianSearchForm(FlaskForm):
    obj_name = StringField("Search term",validators=[DataRequired()])
    obj_type = RadioField('Search for',choices=[(x,x) for x in ['Book','Author','Section','User']],default='Book')
    submit = SubmitField('Search')
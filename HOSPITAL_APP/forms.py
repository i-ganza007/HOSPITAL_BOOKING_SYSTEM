from flask_wtf import FlaskForm
from wtforms import StringField , EmailField , TelField , IntegerField , PasswordField , SubmitField , SelectField
from wtforms.validators import DataRequired , Length , Email , EqualTo , Regexp , NumberRange

# Form for Registering new Users

class RegistrationForm(FlaskForm):
    first_name = StringField('First-Name', validators=[DataRequired(), Length(min=3)])
    last_name = StringField('Last-Name', validators=[DataRequired(), Length(min=3)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    phone = TelField('Phone Number', validators=[DataRequired(), Length(min=10, max=10), Regexp(r'^07[8932]\d{8}$')])
    id = StringField('ID Number', validators=[DataRequired(), Length(min=16, max=16)])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=16, max=100)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=10)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

# Form for Registering new Doctors

class DocRegistrationForm(FlaskForm):

    speciality_choices = [('Anesthesiology', 'Anesthesiology'), ('Cardiac Medicine', 'Cardiac Medicine'),
                          ('Dental Orthodontics', 'Dental Orthodontics'), ('Dermatology', 'Dermatology'),
                          ('Ear,Nose&Throat', 'Ear,Nose&Throat'), ('Endocrinology', 'Endocrinology'),
                          ('Gastroenterology', 'Gastroenterology'), ('General Internal Medicine', 'General Internal Medicine'),
                          ('Geriatric', 'Geriatric'), ('Hematology', 'Hematology'), ('Imaging & Diagnostic', 'Imaging & Diagnostic'),
                          ('Neonatology', 'Neonatology'), ('Nephrology', 'Nephrology'), ('Neurology', 'Neurology'),
                          ('OBGYN', 'OBGYN'), ('Oncology', 'Oncology'), ('Pediatrics', 'Pediatrics'),
                          ('Plastic Surgery', 'Plastic Surgery'), ('Pulmonology', 'Pulmonology'), ('Urology', 'Urology')]
    first_name = StringField('First-Name', validators=[DataRequired(), Length(min=3)])
    last_name = StringField('Last-Name', validators=[DataRequired(), Length(min=3)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    phone = TelField('Phone Number', validators=[DataRequired(), Length(min=10, max=10), Regexp(r'^07[8932]\d{8}$')])
    speciality = SelectField('Specialisation',validators=[DataRequired()],choices=speciality_choices)
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=10)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

# Form for logging in with email for a user

class EmailLoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=10)])
    submit = SubmitField('Submit')

# Form for logging in with phone number for a user


class NumLoginForm(FlaskForm):
    phone = TelField('Phone Number', validators=[DataRequired(), Length(min=10, max=10)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=10)])
    submit = SubmitField('Submit')

# Form for logging in with email for a doctor

class DocLoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=10)])
    submit = SubmitField('Submit')
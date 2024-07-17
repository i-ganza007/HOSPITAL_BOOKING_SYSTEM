from flask_wtf import FlaskForm
from wtforms import StringField , EmailField , TelField , IntegerField , PasswordField , SubmitField , SelectField
from wtforms.validators import DataRequired , Length , Email , EqualTo , Regexp , NumberRange , ValidationError

from HOSPITAL_APP.models import Doctor, Patient

# Form for Registering new Users

class RegistrationForm(FlaskForm):
    first_name = StringField('First-Name', validators=[DataRequired(), Length(min=3)])
    last_name = StringField('Last-Name', validators=[DataRequired(), Length(min=3)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[DataRequired(), Regexp(r'^07[8932]\d{8}$')])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=10)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')


    def validate_email(self,email):
        patient = Patient.query.filter_by(email=email.data).first()
        if patient:
            raise ValidationError('Patient exists with this email')
        
        
    def validate_password(self,password):
        patient = Patient.query.filter_by(password=password.data).first()
        if patient:
            raise ValidationError('Patient exists with this password')
        
    def validate_phone(self,phone):
        patient = Patient.query.filter_by(phone=phone.data).first()
        if patient:
            raise ValidationError('Patient exists with this Phone number')
        

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

    def validate_email(self,email):
        doctor = Doctor.query.filter_by(email=email.data).first()
        if doctor:
            raise ValidationError('Doctor exists with this email')
        
    def validate_id(self,id):
        doctor =  Doctor.query.filter_by(id=id.data).first()
        if doctor:
            raise ValidationError('Doctor exists with this ID number')
        
    def validate_password(self,password):
        doctor =  Doctor.query.filter_by(password=password.data).first()
        if doctor:
            raise ValidationError('Doctor exists with this password')
        
    def validate_phone(self,phone):
        doctor =  Doctor.query.filter_by(phone=phone.data).first()
        if doctor:
            raise ValidationError('Doctor exists with this Phone number')

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
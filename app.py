from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, redirect , render_template , url_for , flash , get_flashed_messages
import flask
from flask_wtf import FlaskForm
from sqlalchemy import false
from wtforms import StringField , EmailField , TelField , IntegerField , PasswordField , SubmitField , SelectField
from wtforms.validators import DataRequired , Length , Email , EqualTo , Regexp , NumberRange

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ef1ce2d11f318f31eb50'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Table for registering patients
class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    phone = db.Column(db.String(10), nullable=False, unique=True)
    ID_number = db.Column(db.Integer, nullable=False, unique=True)  # Changed from 'ID' to 'ID_number'
    age = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(), nullable=False, unique=True)
    date_joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    appointments = db.relationship('Appointment', backref='patient_ref', lazy=True)  # Changed backref to 'patient_ref'

# Table for registering doctors
class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    phone = db.Column(db.String(10), nullable=False, unique=True)
    speciality = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False, unique=True)
    date_joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    appointments = db.relationship('Appointment', backref='doctor_ref', lazy=True)  # Changed backref to 'doctor_ref'

# Table for appointments
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctor.id'), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    # Define relationships explicitly with unique backref names
    patient = db.relationship('Patient', foreign_keys=[patient_id], backref=db.backref('appointments', lazy=True))
    doctor = db.relationship('Doctor', foreign_keys=[doctor_id], backref=db.backref('appointments', lazy=True))


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

specialities = [
    {'title':'Dental Services','content':'Specialises in the prevention and treatment of oral disease, including diseases of the teeth and supporting structures and diseases of the soft tissues of the mouth.'},
    {'title':'Dermatology','content':'Specialises in the diagnosis and treatment of skin disorders.'},
    {'title':'Ear,Nose&Throat','content':'A medical specialty which is focused on the ears, nose, and throat. '},
    {'title':'Endocrinology','content':'Responsible for evaluating diabetes, bone loss, and a range of hormonal issues, including hormones from the pituitary, adrenal, and thyroid glands as well as reproductive organs'},
    {'title':'Gastroenterology','content':'Specialises in the study of the normal function and diseases of the esophagus, stomach, small intestine, colon and rectum, pancreas, gallbladder, bile ducts and liver'},
    {'title':'Geriatric','content':'Specialty focused on providing care for the unique health needs of the elderly'},
    {'title':'Nephrology','content':'Specialises in chronic kidney problems and diseases.'},
    {'title':'Neurology','content':'Specialises in the study and treatment of disorders of the nervous system'},
    {'title':'OBGYN','content':'Specialises in pregnancy , childbirth and female reproductive system'},
    {'title':'Oncology','content':'Specializes in the diagnosis and treatment of cancer.'},
    {'title':'Pediatrics','content':'Specialises in children'},
    {'title':'Plastic Surgery','content':'Specialty involving the restoration, reconstruction, or alteration of the human body.'},
    {'title':'Pulmonology','content':'Specializes in the respiratory system.'},
    {'title':'Urology','content':'Specialises in the diseases of the male and female urinary tract (kidneys, ureters, bladder and urethra).'}
]

# home route

@app.route('/home')
def home():
    return render_template('home.html',title='Home Page',specialities=specialities)

# registering user route

@app.route('/register/user',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created !','success')
        return redirect('emailLogin')
    return render_template('register.html',title='Register Page',form=form)

# registering doctors route

@app.route('/register/doctors',methods=['GET','POST'])
def doc_register():
    form = DocRegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created !','success')
        return redirect('docLogin')
    return render_template('doctors-reg.html',title='Doctors Registration Page',form=form)

# user email login route
@app.route('/', methods=['GET', 'POST'])
@app.route('/login/user-email-login', methods=['GET', 'POST'])
def emailLogin():
    form = EmailLoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == 'kigali123':
            flash('Successfully logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Incorrect email or password', 'danger')
    return render_template('email-login.html', title='Login Page', form=form)

# user phone login route
@app.route('/login/user-num-login',methods=['GET','POST'])
def numLogin():
    form = NumLoginForm()
    if form.validate_on_submit():
        flash('Successfully logged in!','success')
        return redirect(url_for('home'))
    return render_template('num-login.html',title='Login Page',form=form)

# login doctors route
@app.route('/login/doctors',methods=['GET','POST'])
def doc_login():
    form = DocLoginForm()
    return render_template('doc-login.html',title='Doctors Login Page',form=form)

# about route
@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html',title='About Page')
# profile about
@app.route('/profile',methods=['GET','POST'])
def profile():
    return render_template('profile.html',title='Profile Page')



if __name__=='__main__':
    app.run(debug=True)
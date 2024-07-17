from flask import render_template, url_for, flash, redirect
from HOSPITAL_APP.forms import DocLoginForm , DocRegistrationForm , EmailLoginForm , NumLoginForm , RegistrationForm
from HOSPITAL_APP.models import Appointment, Patient , Doctor
from HOSPITAL_APP import bcrypt , app , db
from flask_login import login_user


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
        hashed_user_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        patient = Patient(first_name = form.first_name.data,last_name=form.last_name.data,email=form.email.data,phone=form.phone.data,age=form.age.data,password=hashed_user_pass)
        db.session.add(patient)
        db.session.commit()
        flash(f'Account created !','success')
        return redirect('emailLogin')
    return render_template('register.html',title='Register Page',form=form)

# registering doctors route

@app.route('/register/doctors',methods=['GET','POST'])
def doc_register():
    form = DocRegistrationForm()
    if form.validate_on_submit():
        hashed_doctor_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        doctor = Doctor(first_name = form.first_name.data,last_name=form.last_name.data,email=form.email.data,phone=form.phone.data,password=hashed_doctor_pass,speciality=form.speciality.data)
        db.session.add(doctor)
        db.session.commit()
        flash(f'Account created !','success')
        return redirect('docLogin')
    return render_template('doctors-reg.html',title='Doctors Registration Page',form=form)

# user email login route
@app.route('/', methods=['GET', 'POST'])
@app.route('/login/user-email-login', methods=['GET', 'POST'])
def emailLogin():
    form = EmailLoginForm()
    if form.validate_on_submit():
        patient = Patient.query.filter_by(email=form.email.data).first()
        if patient and bcrypt.check_password_hash(patient.password,form.password.data):
            flash('Successfully logged in!', 'success')
            login_user(patient)
            return redirect(url_for('home'))
        else:
            flash('Incorrect email or password', 'danger')
    return render_template('email-login.html', title='Login Page', form=form)

# user phone login route
@app.route('/login/user-num-login',methods=['GET','POST'])
def numLogin():
    form = NumLoginForm()
    if form.validate_on_submit():
        patient = Patient.query.filter_by(phone=form.phone.data).first()
        if patient and bcrypt.check_password_hash(patient.password,form.password.data):
           flash('Successfully logged in!','success')
           login_user(patient)
           return redirect(url_for('home'))
        else:
            flash('Incorrect phone  umber or password', 'danger')
    return render_template('num-login.html',title='Login Page',form=form)

# login doctors route
@app.route('/login/doctors',methods=['GET','POST'])
def doc_login():
    form = DocLoginForm()
    if form.validate_on_submit():
        doctor = Doctor.query.filter_by(email=form.email.data).first()
        if doctor and bcrypt.check_password_hash(doctor.password,form.password.data):
            login_user(doctor)
            redirect(url_for('home.html'))
        else:
            flash('Login Unsuccessfull')
    return render_template('doc-login.html',title='Doctors Login Page',form=form)

# about route
@app.route('/about',methods=['GET'])
def about():
    return render_template('about.html',title='About Page')
# profile about
@app.route('/profile',methods=['GET','POST'])
def profile():
    return render_template('profile.html',title='Profile Page')
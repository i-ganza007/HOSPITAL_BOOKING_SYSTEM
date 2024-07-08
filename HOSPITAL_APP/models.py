from datetime import datetime
from HOSPITAL_APP import db

class Patient(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    phone = db.Column(db.String(10), nullable=False, unique=True)
    ID_number = db.Column(db.Integer, nullable=False, unique=True)  # Changed from 'ID' to 'ID_number'
    age = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(), nullable=False, unique=True)
    date_joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    # Use a unique backref name for Patient's appointments
    patient_appointments = db.relationship('Appointment', backref='patient', lazy=True)

    def __repr__(self) -> str:
        return f"('{self.first_name}', '{self.last_name}', '{self.email}'"

# Table for registering doctors
class Doctor(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    phone = db.Column(db.String(10), nullable=False, unique=True)
    speciality = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False, unique=True)
    date_joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    # Use a unique backref name for Doctor's appointments
    doctor_appointments = db.relationship('Appointment', backref='doctor', lazy=True)

    def __repr__(self) -> str:
        return f"('{self.first_name}', '{self.last_name}', '{self.speciality}'"

# Table for appointments
class Appointment(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    patient_id = db.Column(db.Integer(), db.ForeignKey('patient.id'), nullable=False)
    doctor_id = db.Column(db.Integer(), db.ForeignKey('doctor.id'), nullable=False)
    date_created = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow())
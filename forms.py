from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=150)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class ServiceBookingForm(FlaskForm):
    bike_model = StringField('Bike Model', validators=[DataRequired()])
    service_type = SelectField('Service Type', choices=[
        ('General Service', 'General Service'),
        ('Oil Change', 'Oil Change'),
        ('Brake Check', 'Brake Check'),
        ('Full Service', 'Full Service')
    ], validators=[DataRequired()])
    booking_date = DateField('Booking Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Book Service')

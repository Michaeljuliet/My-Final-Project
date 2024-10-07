from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, DecimalField, SubmitField, StringField, RadioField
from wtforms.validators import DataRequired, NumberRange, Email, Length, ValidationError

class SurveyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=100)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    age = IntegerField('Age', validators=[DataRequired(), NumberRange(min=18, max=120)])
    gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], validators=[DataRequired()])
    marital_status = RadioField('Marital Status', choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed')], validators=[DataRequired()])
    education = SelectField('Education Level', choices=[
        ('high_school', 'High School'),
        ('bachelors', 'Bachelor\'s Degree'),
        ('masters', 'Master\'s Degree'),
        ('phd', 'PhD'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    employment_status = SelectField('Employment Status', 
                                    choices=[
                                        ('', 'Select'),
                                        ('employed', 'Employed'),
                                        ('self_employed', 'Self Employed'),
                                        ('unemployed', 'Unemployed')
                                    ],
                                    validators=[DataRequired()])
    occupation = StringField('Occupation', validators=[DataRequired(), Length(max=100)])
    income = DecimalField('Annual Income (Naira)', validators=[DataRequired(), NumberRange(min=0)])
    
    # Expenses
    utilities = DecimalField('Utilities (Naira)', validators=[NumberRange(min=0)])
    shopping = DecimalField('Shopping (Naira)', validators=[NumberRange(min=0)])
    healthcare = DecimalField('Healthcare (Naira)', validators=[NumberRange(min=0)])
    entertainment = DecimalField('Entertainment (Naira)', validators=[NumberRange(min=0)])
    school_fees = DecimalField('School fees (Naira)', validators=[NumberRange(min=0)])
        
    submit = SubmitField('Submit')
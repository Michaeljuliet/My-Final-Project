from flask import Blueprint, flash, redirect, url_for, render_template
from app import mongo
from app.forms import SurveyForm

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def survey_form():
    form = SurveyForm()
    if form.validate_on_submit():
        # Keep the existing data collection logic
        user_data = {
            'name': form.name.data,
            'email': form.email.data,
            'age': form.age.data,
            'gender': form.gender.data,
            'marital_status': form.marital_status.data,
            'education': form.education.data,
            'employment_status': form.employment_status.data,
            'occupation': form.occupation.data,
            'income': float(form.income.data),
            'expenses': {
                'utilities': float(form.utilities.data or 0),
                'shopping': float(form.shopping.data or 0),
                'healthcare': float(form.healthcare.data or 0),
                'entertainment': float(form.entertainment.data or 0),
                'school_fees': float(form.school_fees.data or 0),
            }
        }
        mongo.db.survey_responses.insert_one(user_data)
        flash('Thank you for submitting the form', 'success')
        return redirect(url_for('main.survey_form'))
    return render_template('simple_survey.html', form=form)

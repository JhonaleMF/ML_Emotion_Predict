from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
#from wtforms.validators import DataRequired



class ValidateDate(FlaskForm):
    submit = SubmitField("Submit")

# class ValidateFile(FlaskForm):
#     file = FileField("Retrain file", validators=[DataRequired(message="Debes subir un archivo .csv")])
#     submit = SubmitField("Submit")

# class SubmitRetrain(FlaskForm):
#     submit = SubmitField("Submit")
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import Email, Length, DataRequired, Regexp, NumberRange
from hw4.validators import number_length

app = Flask(__name__)
app.config["WTF_CSRF_ENABLED"] = False


class RegistrationForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email(message="Invalid email format")])
    phone = IntegerField('phone',
                         validators=[DataRequired(),
                                     NumberRange(min=0, message='Phone number must be positive integer'),
                                     number_length(min_length=7, max_length=11,
                                                   message="Phone number must be 11 digits")])
    name = StringField('name', validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])
    index = IntegerField('index',
                         validators=[DataRequired(), NumberRange(min=0, message='Phone number must be positive integer')])
    comment = StringField('comment')


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f"Successfully registered user {email} with phone +7{phone}"

    return f"Invalid input, {form.errors}", 400


if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)

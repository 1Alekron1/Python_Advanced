from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired, ValidationError
from typing import Optional


# Валидатор как функция
def number_length(min_length: int, max_length: int, message: Optional[str] = None):
    def _number_length(form: FlaskForm, field: IntegerField):
        number = field.data
        if number is not None:
            if not (min_length <= len(str(number)) <= max_length):
                raise ValidationError(message or f'Number must be between {min_length} and {max_length} digits long.')

    return _number_length


# Валидатор как класс
class NumberLength:
    def __init__(self, min_length: int, max_length: int, message: Optional[str] = None):
        self.min_length = min_length
        self.max_length = max_length
        self.message = message

    def __call__(self, form: FlaskForm, field: IntegerField):
        number = field.data
        if number is not None:
            if not (self.min_length <= len(str(number)) <= self.max_length):
                raise ValidationError(
                    self.message or f'Number must be between {self.min_length} and {self.max_length} digits long.')


# Использование валидаторов
class MyForm(FlaskForm):
    phone1 = IntegerField(
        validators=[InputRequired(), number_length(7, 10, 'Phone number must be between 7 and 10 digits long.')])
    phone2 = IntegerField(
        validators=[InputRequired(), NumberLength(7, 10, 'Phone number must be between 7 and 10 digits long.')])


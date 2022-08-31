from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, NumberRange
# from wtforms.fields.html5 import IntegerField, DecimalField
from wtforms.widgets.html5 import NumberInput
class Apartment(FlaskForm):
    bedrooms = IntegerField('Quartos', validators=[NumberRange(0, 100, message='Aceitos apenas números entre 0 e 100')], widget=NumberInput(min=0, max=100, step=1))
    toilets = IntegerField('Banheiros', validators=[NumberRange(0, 100, message='Aceitos apenas números entre 0 e 100')], widget=NumberInput(min=0, max=100, step=1))
    suites = IntegerField('Suites', validators=[NumberRange(0, 100, message='Aceitos apenas números entre 0 e 100')], widget=NumberInput(min=0, max=100, step=1))
    parking = IntegerField('Vagas de estacionamento', validators=[NumberRange(0, 100, message='Aceitos apenas números entre 0 e 100')] , widget=NumberInput(min=0, max=100, step=1))
    area = IntegerField("Area (M²)", validators=[NumberRange(0, 100, message='Aceitos apenas números entre 0 e 100')] , widget=NumberInput(min=0, max=100, step=1))
    furnished = BooleanField("Apartamento é mobiliado?", )
    swimming_pool = BooleanField("Tem piscina?", )
    elevator = BooleanField("Tem elevador?", )
    neighborhood = StringField('Bairro', validators=[DataRequired('Item obrigatório')])
    submit = SubmitField('Enviar')


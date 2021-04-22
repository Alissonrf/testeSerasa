from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired, ValidationError
from app import db
from app.model.models import EmpresaModel
'''
Este arquivo contém os formulários para adiconar uma empresa e para
adicionar notas e débitos uma empresa
'''

class FormEmpresa(FlaskForm):
    '''Formulário para adicionar empresas manualmente no banco

    Atributes
    ---------
    nome : str
        Campo para adicionar o nome da empresa a se adicionar
    submit : boolean
        Botão para enviar o formulário 
    '''
    nome = StringField("Nome da empresa", 
                       validators=[InputRequired("Coloque o nome da empresa")])
    submit = SubmitField("Confirmar")


class FormNotaDebito(FlaskForm):
    '''Formulário para adicionar notas e débitos a uma empresa

    Atributes
    ---------
    notas : int
        Campo para adicionar a quantidade de notas emitidas pela empresa
    debitos : int
        Campo para adicionar a quantidade de débitos emitidos pela empresa
    submit : boolean
        Botão para enviar o formulário
    '''
    notas = IntegerField("Notas", 
                         validators=[InputRequired("Digite um número inteiro")])
    debitos = IntegerField("Débitos", 
                           validators=[InputRequired("Digite um número inteiro")])
    submit = SubmitField("Confirmar")

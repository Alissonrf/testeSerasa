from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.controller.config import Config

'''
Arquivo inicializador do flask no programa
'''

app = Flask(__name__, template_folder="view")
app.config.from_object(Config)
db = SQLAlchemy(app)

from app.model import forms
from app.model import models
from app.controller import routes
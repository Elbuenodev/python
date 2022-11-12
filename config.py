#pip install Flask-SQLAlchemy
#pip install mysqlclient

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'chave secreta'

#configuração da extensão SQLALCHEMY do Flask
#no mysql command line: CREATE DATABASE bancodados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:softgraf@localhost:3306/bancodados'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#configuração do sistema de CAPTCHA
app.config['RECAPTCHA_USE_SLL'] = False
app.config['RECAPTCHA_PUBLIC_KEY'] = '6Lc7oaYhAAAAAP4-hpS6q1de7URkOoViFPbAV__s'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6Lc7oaYhAAAAAPZ5iNowGhJyC7EioHnZtsSPQjGt'
app.config['RECAPTCHA_OPTIONS'] = {'theme': 'white'}

#cria um objeto db para acesso ao banco de dados da aplicação
db = SQLAlchemy(app)

#somente para o teste do sistema
lista = []
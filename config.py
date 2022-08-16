#Framework ORM: FLASK-SQLALCHEMY

#site oficial
#https://flask-sqlalchemy.palletsproject.com
#No terminal do pycharm  digita:
#pip install Flask Flask-SQLAlchemy
#ERRO DE SEGURANÇA NO PAINEL DO PYCHARM:Mudar a politica de segurança do powershell
#1-Executar o powershell no modo administrador
#2-set-executionpolicy Remotesigned
#3-a (All)

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Configurando o acesso so bancvo de dados SQLAlchemy
#basedir = 'D:\curso Python\projeto_Alchemy'
basedir = os.path.abspath(os.path.dirname(__file__))
uri ='sqlite:///' + os.path.join(basedir, 'database.bd')

#para Mysql
#mysql://username:password@host:port/database_name
#exemmplo: 'mysql://root:senha@localhost:3306/nome_banco'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#cria o banco de dados do app
db = SQLAlchemy(app)
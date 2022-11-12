#pip install Flask_WTF
#pip install wtforms[email]
# pip install wtforms-recaptcha

from flask_wtf import FlaskForm, RecaptchaField

from wtforms import validators, ValidationError, StringField, IntegerField, SubmitField,\
                    PasswordField, EmailField

from wtforms.validators import Length, DataRequired, NumberRange, Email, EqualTo, Optional






class FormCadastro(FlaskForm):
    nome = StringField('Nome', validators=[Length(min=6, max=60),
                                DataRequired('Faltou digitar o nome')])

    idade = IntegerField("Idade", validators=[NumberRange(min=18, max=65),
                                              DataRequired('Faltou idade')])

    email = EmailField('Email', validators=[Length(min=6, max=60),
                                            Email(message='Entre com um e-mail válido'),
                                            DataRequired()
                                            ])

    senha = PasswordField('Senha', validators=[DataRequired(),
                                               Length(min=6, message='Selecione uma senha forte')
                                               ])

    confirmacao = PasswordField('Confirme sua senha',
                                validators=[DataRequired(),
                                EqualTo('senha', message='Senhas devem corresponder')])

    recaptcha = RecaptchaField()


    submit = SubmitField('Enviar')
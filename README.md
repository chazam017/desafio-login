# configuração do Banco de Dados
# no arquivo settings.py, configure a conexão com o MySQL:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'meu_banco',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# instalação

# ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
# dependências
pip install -r requirements.txt
# migração
python manage.py migrate
# super-usuário
python manage.py createsuperuser
# iniciação do servidor
python manage.py runserver

# configuração de email
# para enviar e-mails de confirmação, configure as credenciais SMTP no settings.py:

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.seuprovedor.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'seu-email@dominio.com'
EMAIL_HOST_PASSWORD = 'sua-senha'

# esse projeto está utilizando a licença MIT, sinta-se a vontade para alterar o código :)

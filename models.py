from django.db import models

# modelos de Usuário (models.py)
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

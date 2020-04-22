from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    '''
    Пользовательская модель идентификации.
    
    '''
    
    class Meta(AbstractUser.Meta):
        pass


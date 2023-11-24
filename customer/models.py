from django.contrib.auth.models import User, AbstractUser
from django.db import models
from simple_history.models import HistoricalRecords


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField('Имя', max_length=50, default='')
    last_name = models.CharField('Фамилия', max_length=50, default='')
    email = models.EmailField('Электронная почта', default='', unique=True)
    gender_choices = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
    )
    gender = models.CharField('Пол', max_length=1, choices=gender_choices, default='M')
    history = HistoricalRecords()
    
    
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return self.email

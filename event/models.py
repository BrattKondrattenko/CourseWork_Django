from django.db import models
from simple_history.models import HistoricalRecords


# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    date = models.DateField(verbose_name="Дата")
    location = models.CharField(max_length=255, verbose_name="Адрес")
    history = HistoricalRecords()
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"


class Ticket(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="Событие")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    history = HistoricalRecords()
    

    def __str__(self):
        return f"{self.event.name} - {self.price}"

    class Meta:
        verbose_name = "Билет"
        verbose_name_plural = "Билеты"

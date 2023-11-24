from django.db import models
from simple_history.models import HistoricalRecords

from customer.models import Customer
from event.models import Ticket


# Create your models here.


class TicketInOrder(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, verbose_name="Билет")
    quantity = models.PositiveIntegerField(verbose_name="Кол-во")
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Билет в заказе"
        verbose_name_plural = "Билеты в заказе"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name="Клиент")
    order_date = models.DateField(verbose_name="Дата заказа", auto_now_add=True)
    entries = models.ManyToManyField(TicketInOrder, verbose_name="Билеты")
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.customer.email} - {self.order_date}"

    def total_price(self):

        tickets = self.entries.all().values_list('ticket_id',
                                                 'quantity')
        total = 0

        if tickets:
            for ticket in tickets:
                ticket_id = ticket[0]
                quantity = ticket[1]
                price = Ticket.objects.get(id=ticket_id).price

                total += quantity * price

        return total

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="Заказ")
    payment_date = models.DateField(verbose_name="Дата оплаты", auto_now_add=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="К оплате")
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Оплата"
        verbose_name_plural = "Оплата"

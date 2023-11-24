from django.shortcuts import render

from order.models import Order, Payment


# Create your views here.
def index(request):
    orders = Order.objects.all()
    return render(request, "orders/orders.html", {"orders": orders})


def payment(request):
    payments = Payment.objects.all()
    return render(request, "orders/payments.html", {"payments": payments})

from django.shortcuts import render

from customer.forms import CustomerForm
from customer.models import Customer


# Create your views here.
def customers(request):
    customer_list = Customer.objects.all()

    return render(request, 'customers/customers.html', {"customers": customer_list})


def add_customer(request):
    error = ''
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()

        else:
            error = 'Форма была неверной'

    form = CustomerForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'form.html', context=data)

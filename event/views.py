from django.shortcuts import render

from event.models import Event, Ticket


# Create your views here.
def index(request):
    events = Event.objects.all()
    return render(request, "events/events.html", {"events": events})


def tickets(request):
    tickets_list = Ticket.objects.all()
    return render(request, "events/tickets.html", {"tickets": tickets_list})



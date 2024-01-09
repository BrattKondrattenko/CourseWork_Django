import datetime

from django.contrib import admin

# Register your models here.

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.resources import ModelResource

from event.models import Ticket, Event
from order.models import Order, Payment


class TicketInline(admin.StackedInline):
    model = Ticket
    extra = 0


class EventResource(ModelResource):
    class Meta:
        model = Event
        fields = ('name', 'date', 'location')

    def dehydrate_date(self, event):
        return f"{event.date}"

    def get_location(self, value):
        return value


# Register your models here.
@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    resource_class = EventResource

    list_display = ('name', 'date', "location")
    list_display_links = ('name',)
    search_fields = ('name',)
    date_hierarchy = "date"
    list_filter = ("date", "location",)
    inlines = [TicketInline]

    def get_export_queryset(self, request):
        return Event.objects.filter(date__gte=datetime.datetime.today())


@admin.register(Ticket)
class TicketAdmin(ImportExportModelAdmin):
    list_display = ('event', 'price')
    raw_id_fields = ("event",)
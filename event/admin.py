from django.contrib import admin

# Register your models here.

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from event.models import Ticket, Event
from order.models import Order, Payment


class TicketInline(admin.StackedInline):
    model = Ticket
    extra = 0


# Register your models here.
@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    list_display = ('name', 'date', "location")
    list_display_links = ('name',)
    search_fields = ('name',)
    date_hierarchy = "date"
    list_filter = ("date", "location",)
    inlines = [TicketInline]


@admin.register(Ticket)
class TicketAdmin(ImportExportModelAdmin):
    list_display = ('event', 'price')
    raw_id_fields = ("event",)

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from customer.models import Customer
from order.models import Order


class OrderInline(admin.StackedInline):
    model = Order
    extra = 1


@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    list_display = ('first_name', 'last_name', "email", 'gender')
    list_display_links = ('first_name',)
    list_filter = ("gender",)
    inlines = [OrderInline]

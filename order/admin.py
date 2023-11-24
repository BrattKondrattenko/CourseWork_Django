from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from order.models import Order, Payment, TicketInOrder


class PaymentInline(admin.StackedInline):
    model = Payment
    extra = 0


@admin.register(TicketInOrder)
class TicketInOrderAdmin(ImportExportModelAdmin):
    list_display = ("ticket", "quantity")


@admin.register(Payment)
class PaymentAdmin(ImportExportModelAdmin):
    list_display = ("order", "payment_amount", "payment_date")
    readonly_fields = ("payment_date",)
    date_hierarchy = "payment_date"


# Register your models here.
@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    list_display = ('customer', 'order_date', "total_price")
    list_display_links = ('customer',)
    readonly_fields = ("order_date",)
    date_hierarchy = "order_date"
    filter_horizontal = ["entries"]
    list_filter = ("customer",)
    inlines = [PaymentInline]

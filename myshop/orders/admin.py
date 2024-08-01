from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'city', 'created', 'paid']
    list_editable = ['paid']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInLine]


admin.site.register(Order, OrderAdmin)
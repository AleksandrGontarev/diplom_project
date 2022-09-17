from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('status', 'delivery_address')
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'quantity')


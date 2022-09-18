from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user_email', 'status', 'delivery_address', 'order_id_in_shop')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'book_store_id', 'quantity')

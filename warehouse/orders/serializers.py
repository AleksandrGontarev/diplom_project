from rest_framework import serializers
from orders.models import Order, OrderItem
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['pk', 'user_email', 'status', 'delivery_address', 'order_id_in_shop']


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['pk', 'order_id', 'book_store_id', 'quantity', 'book_item_id']

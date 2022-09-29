from rest_framework import serializers
from orders.models import Order, OrderItem
from django.contrib.auth.models import User
from books.serializers import BookItemSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class OrderItemSerializer(serializers.ModelSerializer):
    book_item_id = BookItemSerializer(read_only=True, many=True)

    class Meta:
        model = OrderItem
        fields = ['pk', 'order_id', 'book_store_id', 'quantity', 'book_item_id']


class OrderSerializer(serializers.ModelSerializer):
    orderitem = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['pk', 'user_email', 'status', 'delivery_address', 'order_id_in_shop', 'orderitem']



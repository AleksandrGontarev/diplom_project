from rest_framework import serializers
from orders.models import Order, OrderItem
from django.contrib.auth.models import User
from books.serializers import BookItemSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class OrderSerializer(serializers.ModelSerializer):
    # order_id = serializers.HyperlinkedRelatedField(many=True, view_name='orderitem-detail', read_only=True)
    class Meta:
        model = Order
        fields = ['pk', 'status', 'delivery_address', 'user_email', 'order_id_in_shop']


class OrderItemSerializer(serializers.ModelSerializer):
    # book_item_id = serializers.HyperlinkedRelatedField(many=True, view_name='bookitem-detail', read_only=True)
    class Meta:
        model = OrderItem
        fields = ['pk', 'book_store_id', 'quantity']






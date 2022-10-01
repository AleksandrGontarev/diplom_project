from rest_framework import serializers
from orders.models import Order, OrderItem
from django.contrib.auth.models import User
from books.serializers import BookItemSerializer
from books.models import BookItem


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class OrderSerializer(serializers.ModelSerializer):
    order_item = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        source='order',
        view_name='orderitem-detail',
    )

    class Meta:
        model = Order
        # fields = ['pk', 'status', 'delivery_address', 'user_email', 'order_id_in_shop']
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):

    book = serializers.HyperlinkedRelatedField(read_only=True, source='book_id', view_name='book-detail')

    class Meta:
        model = OrderItem
        fields = ['pk', 'book', 'quantity', 'order_id', 'book_id']







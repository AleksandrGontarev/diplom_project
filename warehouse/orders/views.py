from orders.models import Order, OrderItem
from orders.serializers import OrderSerializer, OrderItemSerializer
# from books.serializers import UserSerializer
# from books.models import User
# from books.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets, generics, mixins, status
from rest_framework.response import Response

from rest_framework import permissions


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


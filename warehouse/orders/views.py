from orders.models import Order, OrderItem
from orders.serializers import OrderSerializer, OrderItemSerializer
from rest_framework import viewsets

from rest_framework import permissions


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [permissions.IsAuthenticated]


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    # permission_classes = [permissions.IsAuthenticated]

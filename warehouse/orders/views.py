from orders.models import Order, OrderItem
from orders.serializers import OrderSerializer, OrderItemSerializer
# from books.serializers import UserSerializer
# from books.models import User
# from books.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets

from rest_framework import permissions


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
                          # ,IsOwnerOrReadOnly]


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]
                          # ,IsOwnerOrReadOnly]


# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

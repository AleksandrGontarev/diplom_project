from django.urls import path

from orders.views import OrderOrderItemCreate, OrderDetailView, OrderListView, CartListView

urlpatterns = [
    path('order/new/', OrderOrderItemCreate.as_view(), name='order_new'),

    path('order/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('order/', OrderListView.as_view(), name='order_list'),
    path('orderitem/', CartListView.as_view(), name='cart'),
]

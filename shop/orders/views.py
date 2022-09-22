from django.views.generic import ListView, DetailView, CreateView, View
from orders.models import Order, OrderItem
from django.shortcuts import render, redirect
from users.models import User
from orders.forms import OrderItemFormSet
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django import forms
from django.http import HttpResponse
from django.db import transaction


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    paginate_by = 10
    template_name = 'orders/order_list.html'


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/order_detail.html'


class OrderOrderItemCreate(LoginRequiredMixin, CreateView):
    model = Order
    fields = ['delivery_address']
    success_url = reverse_lazy('order_list')
    template_name = 'orders/order_new.html'

    def get_context_data(self, **kwargs):
        data = super(OrderOrderItemCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['orderitem'] = OrderItemFormSet(self.request.POST)
        else:
            data['orderitem'] = OrderItemFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        orderitem = context['orderitem']
        with transaction.atomic():
            self.object = form.save()

            if orderitem.is_valid():
                orderitem.instance = self.object
                orderitem.save()
        return super(OrderOrderItemCreate, self).form_valid(form)


class OrderItemDetailView(LoginRequiredMixin, DetailView):
    model = OrderItem


class OrderView(View):
    model = Order
    paginate_by = 5

    def get_queryset(self):
        queryset = Order.objects.filter(status='cart').select_related("user_id")
        return queryset


class CartListView(ListView):
    model = OrderItem
    paginate_by = 5
    template_name = 'orders/cart.html'

    def get_queryset(self):
        queryset = OrderItem.objects.select_related("book_id", "order_id")
        return queryset

    def get_context_data(self, **kwargs):
        user = Order.objects.select_related("user_id").get(id=1)
        status = user.status
        context = super().get_context_data(**kwargs)

        context["user"] = user
        context["status"] = status

        return context





from django.views.generic import ListView, DetailView, CreateView
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


# class OrderCreateView(LoginRequiredMixin, CreateView):
#     model = Order
#     fields = ['status', 'delivery_address', 'user_id']
#     template_name = 'orders/order_new.html'
#
#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.user_id = self.request.user
#         self.object.save()
#         return super(OrderCreateView, self).form_valid(form)


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
            self.object = form.save(commit=False)

            if orderitem.is_valid():
                orderitem.instance = self.object
                orderitem.save()
        return super(OrderOrderItemCreate, self).form_valid(form)


class OrderItemDetailView(LoginRequiredMixin, DetailView):
    model = OrderItem


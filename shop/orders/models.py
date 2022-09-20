from django.db import models
from users.models import User
from books.models import Book
from django.urls import reverse


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    ORDER_STATUS = (
        ('c', 'Cart'),
        ('o', 'Ordered'),
        ('s', 'Success'),
        ('f', 'Fail'),
    )

    status = models.CharField(max_length=1, choices=ORDER_STATUS, blank=True, default='o', help_text='Order status')
    delivery_address = models.CharField(max_length=255)

    def __str__(self):
        return self.pk

    def get_absolute_url(self):
        return reverse('order-detail', args=[str(self.pk)])


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()


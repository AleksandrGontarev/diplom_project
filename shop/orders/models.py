from django.db import models


class Order(models.Model):
    # user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    ORDER_STATUS = (
        ('c', 'Cart'),
        ('o', 'Ordered'),
        ('s', 'Success'),
        ('f', 'Fail'),
    )

    status = models.CharField(max_length=1, choices=ORDER_STATUS, blank=True, default='o', help_text='Order status')
    delivery_address = models.CharField(max_length=255, help_text='delivery address')


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    # book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()


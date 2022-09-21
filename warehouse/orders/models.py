from django.db import models
from books.models import BookItem
import uuid


class Order(models.Model):
    user_email = models.EmailField(max_length=254)

    ORDER_STATUS = (
        ('i', 'In_work'),
        ('s', 'Success'),
        ('f', 'Fail'),
    )

    status = models.CharField(max_length=1, choices=ORDER_STATUS, blank=True, default='i', help_text='Order status')
    delivery_address = models.CharField(max_length=255, help_text='delivery address')
    order_id_in_shop = models.IntegerField()

    def __str__(self):
        return str(self.pk)


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name='order_id')
    book_store_id = models.UUIDField(default=uuid.uuid4, primary_key=True,
                                     help_text="The unique identifier for this particular book in the warehouse and "
                                               "shop")
    quantity = models.IntegerField()
    book_item_id = models.ManyToManyField(BookItem)

    def __str__(self):
        return str(self.pk)

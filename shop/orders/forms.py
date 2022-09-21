from django import forms
from orders import models
from django.forms.models import inlineformset_factory


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = models.OrderItem
        exclude = ()


OrderItemFormSet = inlineformset_factory(models.Order, models.OrderItem,
                                         form=OrderItemForm, extra=1)

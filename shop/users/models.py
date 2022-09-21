from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    pass
    # def get_absolute_url(self):
    #     return reverse('profile', args=[str(self.pk)])

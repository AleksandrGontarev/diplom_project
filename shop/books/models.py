from django.db import models

from django.db import models


class Book(models.Model):
    title = models.CharField("title", max_length=255)
    author = models.CharField("author", max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

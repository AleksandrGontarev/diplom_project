from django.contrib import admin
from .models import Author, Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Author)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')


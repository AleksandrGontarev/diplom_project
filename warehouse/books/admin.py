from django.contrib import admin
from .models import Author, Book, BookItem


@admin.register(Author)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')


@admin.register(Book)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id_store', 'price', 'author')


@admin.register(BookItem)
class BookAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'book_id', 'row', 'shelf', 'history')

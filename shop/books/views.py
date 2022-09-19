from django.views.generic import ListView, DetailView
from books.models import Author, Genre, Book


class AuthorsListView(ListView):
    model = Author
    paginate_by = 10
    template_name = 'books/author_list.html'
    # queryset = Author.objects.prefetch_related('book_set')


class AuthorDetailView(DetailView):
    model = Author


class BookListview(ListView):
    model = Book
    paginate_by = 10
    template_name = 'books/book_list.html'
    # queryset = Book.objects.select_related('genre')


class BookDetailView(DetailView):
    model = Book








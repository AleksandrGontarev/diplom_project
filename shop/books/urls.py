from django.urls import path, include
from books import views
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('books/', views.BookListview.as_view(), name='book-list'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorsListView.as_view(), name='author-list'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]

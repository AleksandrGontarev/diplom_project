from books.models import Book, BookItem, Author
from books.serializers import BookSerializer, BookItemSerializer, AuthorSerializer
from django.db.models import Count
from books.serializers import UserSerializer
# from books.models import User
from books.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets

from rest_framework import permissions


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.annotate(books_count=Count('bookitem'))
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsOwnerOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


class BookItemViewSet(viewsets.ModelViewSet):
    queryset = BookItem.objects.all()
    serializer_class = BookItemSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsOwnerOrReadOnly]

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)


# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

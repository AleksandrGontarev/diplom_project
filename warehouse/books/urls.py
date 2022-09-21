from books.views import BookViewSet, BookItemViewSet, AuthorViewSet
                                    # UserViewSet, BookViewSet, BookItemtViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register(r'users', UserViewSet, basename="user")
router.register(r'authors', AuthorViewSet, basename="author")
router.register(r'books', BookViewSet, basename="book")
router.register(r'bookitems', BookItemViewSet, basename="bookitem")

urlpatterns = [
    path('', include(router.urls)),
]

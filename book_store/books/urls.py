from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from books.views import ListBooksView, BooksDetailView

urlpatterns = [
    path('books/', ListBooksView.as_view(), name="books list"),
    path('books/<int:pk>/', BooksDetailView.as_view(), name="books detail")
]

urlpatterns = format_suffix_patterns(urlpatterns)
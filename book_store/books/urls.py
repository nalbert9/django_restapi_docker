from django.urls import path
from .views import ListBooksView

urlpatterns = [
    path('books/', ListBooksView.as_view(), name="books-all")
]
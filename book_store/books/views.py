from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Books
from .serializers import BooksSerializer

class ListBooksView(generics.ListAPIView):
    """
    Get method handler
    """
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
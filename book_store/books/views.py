from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from books.models import Books
from books.serializers import BooksSerializer


class ListBooksView(generics.ListAPIView):
    """
    Retrieve  get, post.
    """
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    permission_classes = [IsAdminUser]

    @api_view(['GET', 'POST'])
    def book_list(self, request):
        if request.method == 'GET':
            queryset = self.get_queryset()
            serializer = BooksSerializer(queryset, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            book = Books.objects.create(title=request.data["title"],
                                        book_author=request.data["book_author"])
            return Response(data=BooksSerializer(book).data,
                            status=status.HTTP_201_CREATED)
                            
class BooksDetailView(generics.RetrieveUpdateDestroyAPIView):

    @api_view(['GET', 'PUT', 'POST', 'DELETE'])
    def book_detail(self, request, pk):
        """
        Retrieve, update or delete a code snippet.
        """
        try:
            queryset = Books.objects.get(pk=pk)
        except Books.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            queryset = self.get_queryset()
            serializer = BooksSerializer(queryset, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            book = Books.objects.create(title=request.data["title"],
                                        book_author=request.data["book_author"])
            return Response(data=BooksSerializer(book).data,
                            status=status.HTTP_201_CREATED)

        elif request.method == 'PUT':
            serializer = BooksSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            queryset.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

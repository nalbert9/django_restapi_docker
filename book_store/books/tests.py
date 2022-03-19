from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Books
from .serializers import BooksSerializer

# Test for views
class BaseViewTests(APITestCase):
    client = APIClient()

    @staticmethod
    def create_book(title="", book_author=""):
        if title != "" and book_author != "":
            Books.objects.create(title=title, book_author=book_author)

    def sample_books(self):
        self.create_book("The Grass is Always Greener", "Jeffrey Archer")
        self.create_book("The Signalman", "Charles Dickens")
        self.create_book("The Power of Habit", "Charles Duhigg")
        self.create_book("As a Man Thinketh", "James Allen")


class GetAllBooksTests(BaseViewTests):

    def test_get_all_Books(self):
        """
        Testing the existing books added in the sample_books method
        exist when we make a GET request to the Books/ endpoint
        """
        # API endpoint
        response = self.client.get(
            reverse("books-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Books.objects.all()
        serialized = BooksSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

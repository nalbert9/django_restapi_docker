from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITesCase, APIClient
from rest_framework.views import status
from .models import Books
from .serializers import BooksSerializer

# Test for views

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_book(title="", book_author=""):
        if title != "" and book_author != "":
            Books.objects.create(title=title, book_author=book_author)

    def setUp(self):
        # add test data
        self.create_book("The Grass is Always Greener", "Jeffrey Archer")
        self.create_book("The Signalman", "Charles Dickens")
        self.create_book("The Power of Habit", "Charles Duhigg")
        self.create_book("As a Man Thinketh", "James Allen")


class GetAllBooksTest(BaseViewTest):

    def test_get_all_Books(self):
        """
        This test ensures that all Books added in the setUp method
        exist when we make a GET request to the Books/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("Books-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Books.objects.all()
        serialized = BooksSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

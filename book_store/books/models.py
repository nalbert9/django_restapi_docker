from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=255, null=False)
    book_author = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.book_author)
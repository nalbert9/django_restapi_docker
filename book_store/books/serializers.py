from rest_framework import serializers
from books.models import Books

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['title', 'book_author']
    
    def create(self, validated_data):
        return Books.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.book_author = validated_data.get("book_author", instance.book_author)
        instance.save()
        return instance
__author__ = 'Morya Jr'

from django.forms import widgets
from rest_framework import serializers
from bookstore.models import Prices, Books, Authors

class PricesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prices
        fields = ('book_type', 'price')
class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ('name',)
class BooksSerializer(serializers.ModelSerializer):
    authors = AuthorsSerializer()
    prices = PricesSerializer(many=True)
    title = serializers.CharField(max_length=100)
    publication_date = serializers.DateField()
    publisher = serializers.CharField(max_length=50)
    summary = serializers.CharField(max_length=500)
    purchase_link = serializers.URLField()
    cover_img = serializers.URLField()
    class Meta:
        model = Books
        fields = ('id', 'title', 'authors', 'publication_date',
                  'publisher', 'summary', 'prices', 'purchase_link', 'cover_img')

    def create(validated_data):
        price_data = validated_data.pop('prices')
        author_data = validated_data.pop('authors')
        book = Books.objects.create(**validated_data)
        Prices.objects.create(book=book, **price_data)
        Authors.objects.create(book=book, **author_data)
        return book


    def update(self, instance, validated_data):
        price_data = validated_data.pop('price')
        author_data = validated_data.pop('author')
        price = instance.price
        author = instance.author
        instance.id = validated_data.get('id', instance.id)
        instance.title = validated_data.get('title', instance.title)
        instance.publication_date = validated_data.get('publication_date', instance.publication_date)
        instance.publisher = validated_data.get('publisher', instance.publisher)
        instance.summary = validated_data.get('summary', instance.summary)
        instance.purchase_link = validated_data.get('purchase_link', instance.purchase_link)
        instance.cover_img = validated_data.get('cover_img', instance.cover_img)
        instance.save()

        author.name = author_data.get('name:', author.name)
        author.save()

        price.book_type = price_data.get('book_type:', price.book_type)
        price.price = price_data.get('price: $', price.price)
        price.save()



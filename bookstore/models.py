__author__ = 'Morya Jr'

from django.db import models

# Create your models here.
class Authors(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Prices(models.Model):
    book_type = models.CharField(max_length=50)
    price = models.FloatField()
    def __str__(self):
        return self.book_type + ': ' + str(self.price)

class Books(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Authors)
    publication_date = models.DateField()
    publisher = models.CharField(max_length=50)
    summary = models.TextField()
    prices = models.ManyToManyField(Prices)
    purchase_link = models.URLField()
    cover_img = models.URLField()
    def __str__(self):
        return self.title

from django.db import models


class Author(models.Model):
    aname = models.CharField(max_length=20)

class Book(models.Model):
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    bname = models.CharField(max_length=30)
    price = models.IntegerField()
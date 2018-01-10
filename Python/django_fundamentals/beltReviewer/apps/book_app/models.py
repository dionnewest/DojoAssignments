from __future__ import unicode_literals

from django.db import models
from ..login_reg.models import *

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return "Book #{}, title: {}, author: {}".format(self.id, self.title, self.author)

class Review(models.Model):
    content = models.TextField(max_length=None)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    users = models.ForeignKey('login_reg.User', related_name='user_review')
    books = models.ForeignKey(Book, related_name='book_review')

    def __repr__(self):
        return "Review #{}, {}, {}, {}, {}".format(self.id, self.content, self.rating, self.users.name, self.books.title)

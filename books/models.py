from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User



# Create your models here.






class Book(models.Model):
    author=models.ForeignKey('Author',related_name="book_author",on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    publication_date=models.DateTimeField(default=timezone.now)
    price=models.DecimalField(max_digits=10,decimal_places=3)
    
    def __str__(self):
        return self.title

class Author(models.Model):
    name=models.CharField(max_length=100)
    birth_date=models.DateTimeField(default=timezone.now)
    biography=models.TextField(max_length=20000)
    
    def __str__(self):
        return self.name
    

class Review(models.Model):
    reviewer_name=models.CharField(max_length=100)
    content=models.TextField(max_length=20000)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    book=models.ForeignKey(Book,related_name="review_book",on_delete=models.CASCADE)
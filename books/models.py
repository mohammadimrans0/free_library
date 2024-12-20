from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='book/uploads', blank=True,)
    description = models.TextField()
    borrow_price = models.IntegerField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    borrowed_by = models.ManyToManyField(User, related_name='borrowed_books', blank=True)

    def __str__(self):
        return self.title
    

class BookBorrow(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"
    

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Reviewed by {self.name}"
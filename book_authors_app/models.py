from django.db import models

# Create your models here.
class Author(models.Model):
    # id INT
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.TextField(default='Not provided')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __repr__(self):
        return f"<Author object: {self.first_name} {self.last_name} ({self.id})>"

class Book(models.Model):
    # id INT
    title = models.CharField(max_length=255)
    desc = models.TextField()
    author = models.ManyToManyField(Author,related_name="books")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __repr__(self):
        return f"<Book object: {self.title} ({self.id})>"

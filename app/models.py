from django.db import models

# Create your models here.

class Library(models.Model):
    Book= models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.Book

class Author(models.Model):
    Book= models.ForeignKey(Library, on_delete= models.CASCADE)
    Author= models.CharField(max_length=50)

    def __str__(self):
        return self.Author                                   
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Genre(models.Model):
    genreName=models.CharField(max_length=255)
    genreDescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.genreName
    
    class Meta:
        db_table='genrename'
        verbose_name_plural='genrenames'

class Author(models.Model):
    authorName=models.CharField(max_length=255)
    authorNotes=models.TextField(null=True, blank=True)
    genreName=models.ForeignKey(Genre, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.authorName
    
    class Meta:
        db_table='authorname'
        verbose_name_plural='authorname'

class Book(models.Model):
    bookTitle=models.CharField(max_length=255)
    genreName=models.ForeignKey(Genre, on_delete=models.DO_NOTHING)
    authorName=models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    pages=models.IntegerField(null=True, blank=True)
    startDate=models.DateField(auto_now=False, auto_now_add=False,null=True, blank=True)
    endDate=models.DateField(auto_now=False, auto_now_add=False,null=True,blank=True)
    bookNotes=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.bookTitle

    class Meta:
        db_table='book'
        verbose_name_plural='books'